from fastapi import FastAPI
from src.routers.task_routes import router as TaskRouter
from src.database.base import Base
from src.database.engine import engine
# from models import task_model  # noqa: F401


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")
app.include_router(TaskRouter, prefix="/tasks", tags=["Tasks"])


@app.get("/")
def home():
    return {"message": "Task Manager API is running!"}
