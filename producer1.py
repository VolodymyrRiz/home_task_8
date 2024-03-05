import faker            
import json
from datetime import datetime
import pika
import mongoengine
from models import Contact
import connect
#import seeds

fake = faker.Faker()
for _ in range(5):
    Contact(fullname=fake.name(),
        mail=fake.email(),
        log_field=False
        ).save()  
    
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='WEB_RIZ', exchange_type='direct')
channel.queue_declare(queue='web_riz_queue', durable=True)
channel.queue_bind(exchange='WEB_RIZ', queue='web_riz_queue')

def create_task():
    contact_ = Contact.objects()   
    for i in contact_:
        message = {
            #'ObjectId': i.id,
            'payload': f'Date: {datetime.now().isoformat}',
            'msg': f"Шановний/а {i.fullname}. Просимо прийти на засідання!"
        }
    
        channel.basic_publish(exchange='WEB_RIZ', routing_key='web_riz_queue', body=json.dumps(message).encode())
connection.close()
       
if __name__ == '__main__':    
    create_task()
           