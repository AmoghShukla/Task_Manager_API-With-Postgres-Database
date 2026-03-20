from fastapi import FastAPI
from utils.Task_logger import logger
from routers.Task_Route import router as task_router

app  = FastAPI(title="Task Manager API")

app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def Home():
    logger.info("API is Running")
    return {"message" : "Your API is Running Now"}

