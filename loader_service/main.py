from fastapi import FastAPI, UploadFile ,File ,Form
import uvicorn

app = FastAPI()

@app.post('/file')
def file_upload(image_id: str = Form(...),file: UploadFile = File(...)):
    print(image_id)
    print(file.file.read())
    return {True : "The file was received successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
