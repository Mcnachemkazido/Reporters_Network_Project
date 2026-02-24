from confluent_kafka import Producer
import json

class KafkaPublisher:
    def __init__(self,bootstrap_servers, topic_name,logger):
        self.bootstrap_servers = bootstrap_servers
        self.topic_name = topic_name
        self.logger = logger


    def publish(self,event):

        producer = Producer({"bootstrap.servers":self.bootstrap_servers})
        value = json.dumps(event).encode("utf-8")

        producer.produce(
            topic=self.topic_name,
            value=value,
            callback=self.delivery_report
        )
        self.logger.info(f'I posted a message to kafka for event: {event['image_id']}')
        producer.flush()


    def delivery_report(self,err, msg):
        if err:
            self.logger.error(f"❌ Delivery failed: {err}")
        else:
            self.logger.info(f"✅ Delivered {msg.value().decode("utf-8")}")
            self.logger.info(f"✅ Delivered to {msg.topic()}  : at offset {msg.offset()}")





