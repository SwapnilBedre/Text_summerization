from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Summarization API is running"}