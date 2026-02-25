import logging
from fastapi import UploadFile ,File ,Form ,APIRouter
from components.GridFSStorage import GridFSStorage
from components.MongoLoaderConfig import MongoLoaderConfig

logging.basicConfig(level=logging.INFO,
    format = '%(asctime)s | %(name)-15s | %(levelname)-8s | %(message)s',
    datefmt='%H:%M:%S')

logger = logging.getLogger(__name__)
logger.info('🤩🤩I started running the server that sendsI started running the server that sends to mongodb')
mongo_uri = MongoLoaderConfig().get_mongo_loader_uri()
grid_storge = GridFSStorage(mongo_uri,logging.getLogger(GridFSStorage.__module__))


route = APIRouter()


@route.post('/file')
def file_upload(image_id: str = Form(...), file: UploadFile = File(...)):
    grid_storge.save_stream_file(image_id,file.file.read())







