import logging
from clean_service.components.CleanConfig import CleanConfig
from clean_service.components.KafkaConsumer import KafkaConsumer
from clean_service.components.TextCleaner import TextCleaner
from clean_service.components.KafkaPublisher import KafkaPublisher

logging.basicConfig(level=logging.INFO,
    format = '%(asctime)s | %(name)-15s | %(levelname)-8s | %(message)s',
    datefmt='%H:%M:%S')

logger = logging.getLogger(__name__)

class CleanOrchestrator:
    def __init__(self,consumer, cleaner, publisher, logger):
        self.consumer = consumer
        self.cleaner = cleaner
        self.publisher = publisher
        self.logger = logger
        self.logger.info('I created the class init.')


    def run(self):
        self.logger.info('Starts creating the loop: receive information, clean and send')
        while True:
            info = self.consumer.start()
            clean_info = self.cleaner.clean("".join(info['raw_text']))
            info['raw_text'] = clean_info
            self.publisher.publish(info)






cfg =  CleanConfig().get_bootstrap_servers()
cons = KafkaConsumer(cfg  ,'RAW','clean',logging.getLogger(KafkaConsumer.__module__))
cln = TextCleaner(logging.getLogger(TextCleaner.__module__))
pub =  KafkaPublisher(cfg  ,'CLEAN',logging.getLogger(KafkaPublisher.__module__))

clean_orchestrator = CleanOrchestrator(cons,cln ,pub,logger)
