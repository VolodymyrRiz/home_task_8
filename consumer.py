import os
import sys
import pika

import time
import json

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello_world')



    def callback(ch, method, properties, body):    
        print(f" [x] Received {body.decode()}")
        # time.sleep(1)
        # print(f" [x] Done: {method.delivery_tag}")
        # ch.basic_ack(delivery_tag=method.delivery_tag)

    #channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello_world', on_message_callback=callback, auto_ack=True)
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
