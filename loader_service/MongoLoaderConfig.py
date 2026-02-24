from dotenv import load_dotenv
import os
load_dotenv()



class MongoLoaderConfig:
    def __init__(self):
        self.mongo_loader_uri = os.getenv('MONGO_URI')

    def get_mongo_loader_uri (self):
        if self.mongo_loader_uri:
            return self.mongo_loader_uri
        return False

