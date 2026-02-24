from dotenv import load_dotenv
import os
load_dotenv()



class IngestionConfig:
    def __init__(self):
        self.mongo_loader_uri = os.getenv('MONGO_LOADER_URL')
        self.image_directory = os.getenv('IMAGE_DIRECTORY')
        self.bootstrap_servers =  os.getenv('BOOTSTRAP_SERVERS')

    def get_mongo_loader_uri (self):
        if self.mongo_loader_uri:
            return self.mongo_loader_uri
        return False

    def get_image_directory(self):
        if self.image_directory:
            return self.image_directory
        return False

    def get_bootstrap_servers(self):
        if self.bootstrap_servers:
            return self.bootstrap_servers
        return False



