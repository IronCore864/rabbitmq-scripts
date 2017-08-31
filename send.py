import pika
from rabbitmq_config import rabbitmq_host, rabbitmq_user, rabbitmq_pwd, rabbitmq_queue

# send a hello world message to rabbitmq

credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pwd)
parameters = pika.ConnectionParameters(
    host=rabbitmq_host, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=rabbitmq_queue)
message = "Hello World"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent {}".format(message))
connection.close()
