from schema.Task_Schema import TaskResponse, TaskCreate, TaskUpdate
from fastapi import APIRouter
from utils.Task_logger import get_logger
from service.task_service import Task_Service

router = APIRouter()
logger = get_logger(__name__)

@router.post("/", response_model=TaskResponse)
def create_task(payload : TaskCreate):
    return Task_Service.Create_Task(payload)

@router.get("/", response_model=TaskResponse)    
def Get_All_Task():
    return Task_Service.Get_All_Task()

@router.get("/", response_model=TaskResponse)
def Get_Task(task_id : int):
    return Task_Service.Get_Task(task_id)

@router.patch("/")
def Update_Task(payload : TaskUpdate):
    return Task_Service.Update_Task(payload)

@router.delete("/")
def Delete_Task(task_id):
    return Task_Service.Delete_Task(task_id)
