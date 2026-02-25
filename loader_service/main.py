import uvicorn
from fastapi import FastAPI
from MongoLoaderOrchestrator import route


app = FastAPI()

app.include_router(route)

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)









