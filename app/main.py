from fastapi import FastAPI, HTTPException
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

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id:int):
    result = storage.get_by_id(task_id)
    if result is None:
        raise HTTPException(status_code=404,detail="Task not found")
    return result