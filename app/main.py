from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}

@app.get("/tasks")
def get_tasks():
    return []