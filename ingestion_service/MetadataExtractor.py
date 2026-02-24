from PIL import Image
import os
import uuid

class MetadataExtractor:
    def __init__(self,logger):
        self.logger = logger


    def extract_metadata(self,image_path):
        image = Image.open(image_path)

        width , height = image.size
        file_format = image.format
        file_size_bytes =  os.path.getsize(image_path)
        self.logger.info(f'I created meta data for image path:{image_path}')
        return {'width':width,'height':height,'file_format':file_format,
                'file_size_bytes':file_size_bytes}


    def generate_image_id(self,image_path):
        self.logger.info(f'I created image id for image path:{image_path}')
        return str(uuid.uuid4())

