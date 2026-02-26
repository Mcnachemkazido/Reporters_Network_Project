from dotenv import load_dotenv
import os
load_dotenv()



class IndexerConfig:
    def __init__(self):
        self.bootstrap_servers =  os.getenv('BOOTSTRAP_SERVERS')
        self.es_uri = os.getenv("ES_URI")


    def get_bootstrap_servers(self):
        if self.bootstrap_servers:
            return self.bootstrap_servers
        return False

    def get_es_uri(self):
        if self.es_uri:
            return self.es_uri
        return False


