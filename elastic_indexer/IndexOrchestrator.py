import logging
from components.IndexerConfig import  IndexerConfig
from components.KafkaConsumer import KafkaConsumer
from components.ElasticsearchClient import ElasticsearchClient


logging.basicConfig(level=logging.INFO,
    format = '%(asctime)s | %(name)-15s | %(levelname)-8s | %(message)s',
    datefmt='%H:%M:%S')

logger = logging.getLogger(__name__)

class IndexOrchestrator:
    def __init__(self,consumer, es_client, logger):
        self.consumer = consumer
        self.ec_client = es_client
        self.logger = logger
        self.count = 0

    def run(self):
        logger.info('☺️🙂🤗I start running the loop I sent to es')
        while True:
            info = self.consumer.start()
            self.ec_client.update_new_data(info)
            self.count += 1
            print(self.count)



cfg =  IndexerConfig()
es = ElasticsearchClient(cfg.get_es_uri(),
'aaa',logging.getLogger(ElasticsearchClient.__module__))

cons = KafkaConsumer(cfg.get_bootstrap_servers(),
['RAW','CLEAN','ANALYTICS'],'es',logging.getLogger(KafkaConsumer.__module__))

index_orchestrator = IndexOrchestrator(cons,es,logger)


