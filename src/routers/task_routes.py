from fastapi import APIRouter, HTTPException, Query, Depends, status
from typing import Optional, List
from src.schema.Task_Schema import TaskCreate, TaskResponse, TaskUpdate
from src.services import task_service
from src.core.logger import get_logger
from sqlalchemy.orm import Session
from src.database.engine import get_db


router = APIRouter()
logger = get_logger(__name__)

@router.post("/create_task", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db : Session=Depends(get_db)):
    logger.info(f"Creating Task : {payload.title}")
    return task_service.create_task(payload, db)

@router.get("/get_all_tasks", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def get_all_tasks(completed: Optional[bool] = Query(None), db : Session=Depends(get_db)):
    return task_service.get_all_tasks(completed, db)

@router.get("/get_task/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def get_task(task_id: int, db : Session=Depends(get_db)):
    task = task_service.get_task(task_id, db)
    logger.info(f"Fetching Task with id : {task_id}")
    if not task:
        logger.warning(f"Task Not Found : {task_id}")
        raise HTTPException(status_code=404, detail="Task Not Found")
    return task


@router.put("/update_task/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, payload: TaskUpdate, db : Session=Depends(get_db)):
    task = task_service.update_task(task_id, payload, db)
    logger.info(f"Updating Task with id : {task_id}")
    if not task:
        logger.warning(f"Task Not Found : {task_id}")
        raise HTTPException(status_code=404, detail="Task Not Found")
    return task

@router.delete("/delete_task/{task_id}")
def delete_task(task_id: int, db : Session=Depends(get_db), status_code=status.HTTP_200_OK):
    logger.info(f"Deleting Task with task_id : {task_id}")
    deleted = task_service.delete_task(task_id, db)
    if not deleted:
        logger.warning(f"Task Not Found : {task_id}")
        raise HTTPException(status_code=404, detail="Task Not Found")

    logger.info(f"Task with id : {task_id}, Deleted Successfully")
    return {"message": "Task Deleted Successfully"}
    
