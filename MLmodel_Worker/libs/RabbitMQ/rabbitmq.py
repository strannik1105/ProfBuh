import logging
import types
from threading import Thread
from pika import PlainCredentials, ConnectionParameters, BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel

from settings import (
    RABBIT_INPUT_QUEUE,
    RABBIT_OUTPUT_EXCHANGE,
    RABBIT_OUTPUT_QUEUE,
    RABBIT_ADDRESS,
    RABBIT_CREDS,
)


class RabbitMQService:
    def __init__(self, address: tuple[str, int], creds: tuple[str, str]):
        self.address = address
        self.creds = PlainCredentials(creds[0], creds[1])
        self.connection = self.connect()
        self.consuming_thread = None

    def connect(self) -> BlockingChannel:
        parameters = ConnectionParameters(
            host=self.address[0],
            virtual_host="/",
            port=self.address[1],
            credentials=self.creds,
            heartbeat=600,
            blocked_connection_timeout=14400,
        )
        channel = BlockingConnection(parameters).channel()
        channel.exchange_declare(RABBIT_OUTPUT_EXCHANGE, "topic", durable=True)
        channel.queue_declare(RABBIT_OUTPUT_QUEUE, durable=True)
        logging.log(1, "RABBIT_MQ: Connected to Rabbit MQ")
        return channel

    def send_message(self, routing_key: str, message: bytes):
        logging.log(1, f"RABBIT_MQ: Sending message {message} to {routing_key}")
        self.connection.basic_publish(RABBIT_OUTPUT_EXCHANGE, routing_key, message)

    def bind(self, routing_key: str, callback: types.FunctionType):
        self.connection.queue_bind(
            queue=RABBIT_OUTPUT_QUEUE,
            exchange=RABBIT_OUTPUT_EXCHANGE,
            routing_key=routing_key,
        )
        self.connection.basic_qos(prefetch_count=1)
        self.connection.basic_consume(
            queue=RABBIT_INPUT_QUEUE, on_message_callback=callback
        )
        try:
            self.consuming_thread = Thread(target=self.connection.start_consuming)
        except Exception as e:
            self.connection.stop_consuming()
            logging.error(f"RABBIT_MQ: Exception on rabbitmq {e}")
            if self.connection.is_open:
                self.connection.close()


rabbitmq = RabbitMQService(RABBIT_ADDRESS, RABBIT_CREDS)
