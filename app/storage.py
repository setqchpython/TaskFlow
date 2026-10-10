from app.models import TaskCreate, TaskResponse, TaskUpdate



_tasks: list[TaskResponse] = []

def get_all() -> list[TaskResponse]:
    return _tasks


def create(task_create: TaskCreate) -> TaskResponse:

    new_id = max((u.id for u in _tasks), default=0) + 1
    payload = task_create.model_dump()
    payload["id"] = new_id
    task = TaskResponse(**payload)
    _tasks.append(task)

    return task


def get_by_id(task_id: int) -> TaskResponse | None:

    for i in _tasks:
        if i.id == task_id:
            return i
    return None

def update(task_id: int, task_update: TaskUpdate) -> TaskResponse | None:

    for i in _tasks:
        if i.id == task_id:
            if task_update.title is not None:
                i.title = task_update.title

            if task_update.description is not None:
                i.description = task_update.description

            if task_update.completed is not None:
                i.completed = task_update.completed

            return i
    return None


def delete(task_id: int) -> TaskResponse | None:

    for idx,task in enumerate(_tasks):
        if task.id == task_id:
            return _tasks.pop(idx)
    return None