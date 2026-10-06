# TaskFlow

REST API для управления задачами


## Стек

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn

## Установка 
```bash
git clone <URL-репозитория>
cd taskflow
py -m venv .venv
pip install -r requirements.txt
```

## Запуск
```bash
uvicorn app.main:app --reload
```

## Endpoints


|Метод|Путь|Описание|
|-----|----|--------|
| GET | /tasks | Список всех задач |
| POST | /tasks | Создать задачу |
| GET | /tasks/{id} | Получить задачу по id |
| PATCH | /tasks/{id} | Частично обновить |
| DELETE | /tasks/{id} | Удалить задачу |



