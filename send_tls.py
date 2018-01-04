import pika
import ssl

ssl_options= {
    "ssl_version": ssl.PROTOCOL_TLSv1_2,
    "ca_certs": "/etc/rabbitmq/testca/cacert.pem",
    "keyfile": "/etc/rabbitmq/client/key.pem",
    "certfile": "/etc/rabbitmq/client/cert.pem",
    "cert_reqs": ssl.CERT_REQUIRED
}

credentials = pika.PlainCredentials('test', 'test')

parameters = pika.ConnectionParameters(
    host='localhost',
    port=5671,
    virtual_host='/',
    ssl=True,
    ssl_options=ssl_options,
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()

