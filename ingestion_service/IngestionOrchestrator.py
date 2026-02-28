import logging
import os
from components.IngestionConfig import IngestionConfig
from components.OCREngine import OCREngine
from components.MetadataExtractor import MetadataExtractor
from components.MongoLoaderClient import MongoLoaderClient
from components.KafkaPublisher import KafkaPublisher


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
        self.logger.info('🤓🤓I start the loop that goes through all the images')
        for file in os.scandir(self.dir_path):
            meta_data = self.metadata_extractor.extract_metadata(file.path)
            text_extraction = self.ocr_engine.extract_text(file.path)
            image_id = self.metadata_extractor.generate_image_id(file.path)

            self.mongo_client.send_to_mongodb_loader(file.path,image_id)

            meta_data["image_id"] = image_id
            meta_data["raw_text"] = text_extraction
            self.publisher.publish(meta_data)

        self.logger.info('💯💯I finished the loop that went'
                         ' through all the images and created data from them.')


ingestion_orchestrator = IngestionOrchestrator()

