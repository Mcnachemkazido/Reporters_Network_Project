from dotenv import load_dotenv
import os
load_dotenv()



class AnalyticsConfig:
    def __init__(self):
        self.bootstrap_servers =  os.getenv('BOOTSTRAP_SERVERS')


    def get_bootstrap_servers(self):
        if self.bootstrap_servers:
            return self.bootstrap_servers
        return False

