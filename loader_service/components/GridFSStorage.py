import pymongo
import gridfs


class GridFSStorage:
    def __init__(self,mongo_uri, logger):
        self.mongo_uri = mongo_uri
        self.logger = logger

        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client['images']
        self.fs = gridfs.GridFS(self.db)


    def save_stream_file(self,image_id ,stream_file):
        file_id = self.fs.put(stream_file, file_id=image_id,description='Text of picture')
        self.logger.info(f'i send to mongodb binary image, image id:{file_id}')







