import json
from confluent_kafka import Consumer



class KafkaConsumer:
    def __init__(self,bootstrap_servers,topic_name, group_id, logger):
        self.bootstrap_servers = bootstrap_servers
        self.topic_name =  topic_name
        self.group_id = group_id
        self.logger = logger

        self.consumer_config = {
            "bootstrap.servers": self.bootstrap_servers,
            "group.id": self.group_id,
            "auto.offset.reset": "earliest"
         }
        self.consumer = Consumer(self.consumer_config)
        self.consumer.subscribe([self.topic_name])


    def start(self):
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                self.logger.error("❌ Error:", msg.error())
                continue
            value = msg.value().decode('utf-8')
            info = json.loads(value)
            self.logger.info(f'I received a new message image id: {info['image_id']}')
            return info




