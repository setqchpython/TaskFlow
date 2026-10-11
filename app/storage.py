from app.models import TaskCreate, TaskResponse, TaskUpdate
from pathlib import Path
import json


p = Path("data/tasks.json")

def _load() -> list[TaskResponse]:

    items = []

    if not p.is_file():
        return []

    if p.stat().st_size == 0:
        return []

    with p.open(encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        items.append(TaskResponse.model_validate(item))
    
    return items




_tasks: list[TaskResponse] = _load()

def get_all() -> list[TaskResponse]:
    return _tasks


def create(task_create: TaskCreate) -> TaskResponse:

    new_id = max((u.id for u in _tasks), default=0) + 1
    payload = task_create.model_dump()
    payload["id"] = new_id
    task = TaskResponse(**payload)
    _tasks.append(task)

    _save()
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

            _save()
            return i
    return None


def delete(task_id: int) -> TaskResponse | None:

    for idx,task in enumerate(_tasks):
        if task.id == task_id:
            removed = _tasks.pop(idx)
            _save()
            return removed

    return None


def _save() -> None:
    p.parent.mkdir(parents=True, exist_ok=True)

    result = [t.model_dump() for t in _tasks]
    with p.open("w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
