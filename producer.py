import json
from datetime import datetime
import pika


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='WEB_RIZ', exchange_type='direct')
channel.queue_declare(queue='web_riz_queue', durable=True)
channel.queue_bind(exchange='WEB_RIZ', queue='web_riz_queue')
    
def create_task(nums: int):
    for i in range(nums):
        message = {
            'id': i,
            'payload': f'Date: {datetime.now().isoformat}'
        }
    
        channel.basic_publish(exchange='WEB_RIZ', routing_key='web_riz_queue', body=json.dumps(message).encode())
    connection.close()
       
if __name__ == '__main__':
    create_task(100)
