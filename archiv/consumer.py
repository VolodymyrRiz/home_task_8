import os
import sys
import pika
import models
from models import Contact
import time
import json
import mongoengine
import connect

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='web_riz_queue', durable=True)

    consumer = 'Rizun'
    def callback(ch, method, properties, body):  
        pk = body.decode()
        task = Contact.objects(id=pk, completed=False).first()
        if task:
            task.update(set__completed=True, set__consumer=consumer)
       
        ch.basic_ack(delivery_tag=method.delivery_tag)
        
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='web_riz_queue', on_message_callback=callback)      
    
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
