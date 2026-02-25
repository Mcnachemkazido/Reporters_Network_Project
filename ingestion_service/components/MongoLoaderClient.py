import requests


class MongoLoaderClient:
    def __init__(self,mongodb_loader_uri,logger):
        self.mongodb_loader_uri = mongodb_loader_uri
        self.logger = logger

    def send_to_mongodb_loader(self,file_path,image_id):
        with open(file_path, 'rb') as f:
            file_to_send = {"file":f}
            data_to_send = {"image_id":image_id}
            response =requests.post(self.mongodb_loader_uri,files=file_to_send,data=data_to_send)

            self.logger.info(f'i send msg to mongodb_loader for image_id:{image_id}\n, '
                             f'this response from fastapi {response.text}')





