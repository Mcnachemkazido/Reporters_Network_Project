from elasticsearch import Elasticsearch
from IndexerConfig import IndexerConfig
class ElasticsearchClient:
    def __init__(self,es_uri, index_name, logger):
        self.es = Elasticsearch(es_uri)
        print('Connected to Elasticsearch!')


c = ElasticsearchClient(IndexerConfig().get_es_uri(),'aaa','aaa')

mapping = {
 'mappings': {
 'properties': {
'image_id': { 'type': 'keyword' },
 'width': { 'type': 'integer' },
 'height': { 'type': 'integer' },
 'file_format': { 'type': 'keyword' },
 'raw_text': { 'type': 'text' },
 'time': { 'type': 'date' },
 'clean_info': { 'type': 'text' },
 'ten_words': { 'type': 'keyword' },
 'weapons': { 'type': 'keyword' },
 'emotion_text': { 'type': 'keyword' }
 }
 }
}
