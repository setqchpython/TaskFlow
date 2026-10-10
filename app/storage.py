from app.models import TaskCreate, TaskResponse



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

