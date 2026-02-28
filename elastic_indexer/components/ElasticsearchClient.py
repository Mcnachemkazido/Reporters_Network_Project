from elasticsearch import Elasticsearch

class ElasticsearchClient:
    def __init__(self,es_uri, index_name, logger):
        self.es = Elasticsearch(es_uri)
        self.index_name =index_name
        self.logger = logger
        self.create_index_if_not_exists()

    def create_index_if_not_exists(self):
        mapping = {
            'mappings': {
                'properties': {
                    'image_id': {'type': 'keyword'},
                    'time': {'type': 'keyword'},
                    'width': {'type': 'integer'},
                    'height': {'type': 'integer'},
                    'file_format': {'type': 'keyword'},
                    'raw_text': {'type': 'text'},
                    'clean_info': {'type': 'text'},
                    'ten_words': {'type': 'keyword'},
                    'weapons': {'type': 'keyword'},
                    'emotion_text': {'type': 'keyword'}
                }
            }
        }

        if not self.es.indices.exists(index=self.index_name):
            self.es.indices.create(index=self.index_name,body=mapping)
            self.logger.info('i create the index')
        else:
            self.logger.info('the index exists')

    def update_new_data(self,data):
        self.es.update(index=self.index_name,id = data['image_id'],body={"doc":data,           # הנתונים לעדכון (אם קיים)
        "doc_as_upsert": True})
        self.logger.info(f"2️⃣I updated new data in es image_id: {data['image_id']}")

    def get_info_by_id(self,image_id):
        res = self.es.get(index=self.index_name,id=image_id)
        return res









