from fastapi import FastAPI
from utils.Task_logger import get_logger
from routers.Task_Route import router as task_router

app  = FastAPI(title="Task Manager API")
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
logger = get_logger(__name__)

@app.get("/")
def Home():
    logger.info("API is Running")
    return {"message" : "Your API is Running Now"}

