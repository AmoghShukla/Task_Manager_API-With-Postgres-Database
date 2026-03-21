from schema.Task_Schema import TaskResponse, TaskCreate, TaskUpdate
from fastapi import APIRouter
from utils.Task_logger import get_logger
from service.task_service import Task_Service

router = APIRouter()
logger = get_logger(__name__)

@router.post("/", response_model=TaskResponse)
def create_task(payload : TaskCreate):
    return Task_Service.Create_Task(payload)

@router.get("/", response_model=list[TaskResponse])
def get_all_tasks():
    return Task_Service.Get_All_Task()

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    return Task_Service.Get_Task(task_id)

@router.patch("/{task_id}")
def Update_Task(task_id: int, payload: TaskUpdate):
    return Task_Service.Update_Task(task_id, payload)

@router.delete("/{task_id}")
def Delete_Task(task_id: int):
    return Task_Service.Delete_Task(task_id)