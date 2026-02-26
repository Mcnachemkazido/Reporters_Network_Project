from components.AnalyticsConfig import AnalyticsConfig
from components.KafkaConsumer import KafkaConsumer
from components.TextAnalyzer import TextAnalyzer
from components.KafkaPublisher import KafkaPublisher

import logging
logging.basicConfig(level=logging.INFO,
            format = '%(asctime)s | %(name)-15s | %(levelname)-8s | %(message)s',
            datefmt='%H:%M:%S')

logger = logging.getLogger(__name__)


class AnalyticsOrchestrator:
    def __init__(self,consumer, analyzer, publisher, logger):
        self.consumer = consumer
        self.analyzer = analyzer
        self.publisher = publisher
        self.logger = logger

    def run(self):
        self.logger.info('😍😘🥰 Starts running the data analysis loop')
        while True:
            info = self.consumer.start()
            analyzed_info = self.analyzer.analysis_flow(info['clean_info'])
            send_info = analyzed_info
            send_info['image_id'] = info['image_id']
            self.publisher.publish(send_info)



cfg =  AnalyticsConfig().get_bootstrap_servers()
cons = KafkaConsumer(cfg,'CLEAN','analysis',logging.getLogger(KafkaConsumer.__module__))
alz = TextAnalyzer(logging.getLogger(TextAnalyzer.__module__))
pub = KafkaPublisher(cfg,'ANALYTICS',logging.getLogger(KafkaPublisher.__module__))

analytics_orchestrator = AnalyticsOrchestrator(consumer=cons,publisher=pub,analyzer=alz,logger=logger)
