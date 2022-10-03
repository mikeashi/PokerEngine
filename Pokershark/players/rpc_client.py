import pika
import uuid
import json
import socket

class rpc_client:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=socket.gethostbyname(socket.gethostname())[:-1] + "1", port=5672))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)
        self.response = None
        self.corr_id = None
    
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
    
    def call(self, method, params = {}):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
                type=method
            ),
            body=json.dumps(params))
        self.connection.process_data_events(time_limit=None)
        return self.response