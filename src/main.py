from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Hello from Irmak's Quiz Bot!"}
