from schema.Task_Schema import Request, Response
from fastapi import APIRouter, HTTPException
from utils.Task_logger import logger
from service.task_service import Task_Service

router = APIRouter()

@router.post("/", response_model=Response)
def create_task(payload : Request):
    return Task_Service.Create_Task(payload)

@router.get("/", response_model=Response)    
def Get_All_Task():
    return Task_Service.Get_All_Task()

@router.get("/", response_model=Response)
def Get_Task(task_id : int):
    return Task_Service.Get_Task(task_id)

@router.patch("/")
def Update_Task(payload):
    return Task_Service.Update_Task(payload)

@router.delete("/")
def Delete_Task(task_id):
    return Task_Service.Delete_Task(task_id)
