import logging
from MongoLoaderConfig import MongoLoaderConfig
from GridFSStorage import GridFSStorage
from MongoLoaderOrchestrator import MongoLoaderOrchestrator



logging.basicConfig(level=logging.INFO,
    format = '%(asctime)s | %(name)-15s | %(levelname)-8s | %(message)s',
    datefmt='%H:%M:%S')

logger = logging.getLogger(__name__)

logger.info('start the main')
mongo_uri = MongoLoaderConfig().get_mongo_loader_uri()
grid_storge = GridFSStorage(mongo_uri,logging.getLogger(GridFSStorage.__module__))
mongodb_loader = MongoLoaderOrchestrator(grid_storge,logging.getLogger(MongoLoaderConfig.__module__))
mongodb_loader.run()











