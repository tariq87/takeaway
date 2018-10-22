import pika
import json

exchange_name = ''
routing_key   = 'queue.message'

def producer(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-server'))
    channel = connection.channel()
    channel.queue_declare(queue=routing_key)
    channel.basic_publish(exchange=exchange_name,
                      routing_key=routing_key,
                      body=message)
    print("Sent : '{}'".format(message))
    connection.close()

def consumer_callback(ch, method, properties, body):
    print("Received : '{}'".format(body.decode('ascii')))

def consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-server'))
    channel = connection.channel()
    channel.queue_declare(queue=routing_key)
    channel.basic_consume(consumer_callback,
                      queue=routing_key,
                      no_ack=True)
    print('Waiting for messages, to exit press CTRL+C')
    channel.start_consuming()
