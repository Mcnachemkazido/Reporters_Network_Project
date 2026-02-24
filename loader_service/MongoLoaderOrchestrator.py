from fastapi import FastAPI, UploadFile ,File ,Form
import uvicorn


class MongoLoaderOrchestrator:
    def __init__(self,storage, logger):
        self.storage = storage
        self.logger = logger

    def handle_upload(self,request_id,request_body):
        self.storage.save_stream_file(request_id ,request_body)


    def run(self):
        app = FastAPI()
        @app.post('/file')
        def file_upload(image_id: str = Form(...), file: UploadFile = File(...)):
            self.handle_upload(image_id,file.file.read())
            self.logger.info(f'I got a new file file_id: {image_id}')
        uvicorn.run(app,port=8001,host='localhost')



