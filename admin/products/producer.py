import pika, json

params = pika.URLParameters('amqps://fruncoiz:HtrEwUS5U0D2x2ZEmMKdkwEyzkJ92Ry5@jackal.rmq.cloudamqp.com/fruncoiz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)