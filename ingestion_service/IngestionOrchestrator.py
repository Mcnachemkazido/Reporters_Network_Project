import logging
from IngestionConfig import IngestionConfig
from OCREngine import OCREngine
from MetadataExtractor import MetadataExtractor
from MongoLoaderClient import MongoLoaderClient
from KafkaPublisher import KafkaPublisher


logging.basicConfig(level=logging.INFO,
            format = '%(asctime)s | %(name)-15s | %(levelname)-8s | %(message)s',
            datefmt='%H:%M:%S')




class IngestionOrchestrator:
    def __init__(self):
        self.config = IngestionConfig()
        self.ocr_engine =  OCREngine(logging.getLogger(OCREngine.__module__))
        self.metadata_extractor = MetadataExtractor(logging.getLogger(MetadataExtractor.__module__))
        self.mongo_client = MongoLoaderClient(self.config.get_mongo_loader_uri(),logging.getLogger(MongoLoaderClient.__module__))
        self.publisher = KafkaPublisher(self.config.get_bootstrap_servers(),'RAW',logging.getLogger(KafkaPublisher.__module__))
        self.dir_path = self.config.get_image_directory()
        self.logger = logging.getLogger(__name__)


    def run(self):
        self.logger.info('start the main')

        sum_files = len(self.dir_path)
        for file in range(sum_files):
            image_id = self.metadata_extractor.generate_image_id(f'{self.dir_path}/tweet_{file}.png')
            meta_data = self.metadata_extractor.extract_metadata(f'{self.dir_path}/tweet_{file}.png')
            text_extraction = self.ocr_engine.extract_text(f'{self.dir_path}/tweet_{file}.png')

            self.mongo_client.send_to_mongodb_loader(f'{self.dir_path}/tweet_{file}.png',image_id)
            self.publisher.publish({"image_id":image_id,"meta_data":meta_data,  "raw_text":text_extraction})

        self.logger.info('finish the main')


ingestion_orchestrator = IngestionOrchestrator()

