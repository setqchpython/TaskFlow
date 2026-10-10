from fastapi import FastAPI
from app.models import TaskCreate,TaskResponse
from app import storage

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}

@app.get("/tasks",response_model=list[TaskResponse])
def get_tasks():
    return storage.get_all()

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    return storage.create(task)