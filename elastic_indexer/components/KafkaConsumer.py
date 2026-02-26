from confluent_kafka import Consumer
from IndexerConfig import IndexerConfig
import logging
import json

logging.basicConfig(level=logging.INFO,
        format = '%(asctime)s | %(name)-15s | %(levelname)-8s | %(message)s',
        datefmt='%H:%M:%S')

logger = logging.getLogger(__name__)

class KafkaConsumer:
    def __init__(self,bootstrap_servers, topics_list, group_id, logger):
        self.bootstrap_servers = bootstrap_servers
        self.topics_list = topics_list
        self.group_id = group_id
        self.logger = logger

        self.config = {"group.id":self.group_id,
                       "bootstrap.servers":self.bootstrap_servers,
                       "auto.offset.reset": "earliest"}
        self.consumer = Consumer(self.config)
        self.consumer.subscribe(self.topics_list)

    def start(self):
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logger.error(f'✖️❌error: {msg.error()}')
                continue
            value = msg.value()
            info = json.loads(value.decode('utf-8'))
            print(info)



k = KafkaConsumer(IndexerConfig().get_bootstrap_servers(),['RAW','CLEAN','ANALYTICS'],'ggg',logger)
k.start()