import logging
from components.CleanConfig import CleanConfig
from components.KafkaConsumer import KafkaConsumer
from components.TextCleaner import TextCleaner
from components.KafkaPublisher import KafkaPublisher

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
        self.logger.info('🤗🤗Starts creating the loop: receive information, clean and send')
        while True:
            info = self.consumer.start()
            time = info['raw_text'].pop(0)
            clean_info = self.cleaner.cleaning_process("".join(info['raw_text']))
            info = {'image_id':info['image_id'],'time':time,'clean_info':clean_info}
            self.publisher.publish(info)






cfg =  CleanConfig().get_bootstrap_servers()
cons = KafkaConsumer(cfg  ,'RAW','clean',logging.getLogger(KafkaConsumer.__module__))
cln = TextCleaner(logging.getLogger(TextCleaner.__module__))
pub =  KafkaPublisher(cfg  ,'CLEAN',logging.getLogger(KafkaPublisher.__module__))

clean_orchestrator = CleanOrchestrator(cons,cln ,pub,logger)
