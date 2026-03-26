from src.core.logger import get_logger
from src.repository import Task_repo as repository

logger = get_logger(__name__)

def create_task(data, db):
    return repository.create(data, db)


def get_all_tasks( db, completed: bool = None):
    return repository.get_all(completed, db)


def get_task(task_id : int, db):
    return repository.get_by_id(task_id, db)


def update_task(task_id: int, data, db):
    return repository.update(task_id, data, db)
    

def delete_task(task_id: int, hard: bool, db):
    if hard:
        logger.info(f"Performing Hard Delete for Task with id : {task_id}")
        return repository.delete(task_id, db)
    
    logger.info(f"Performing Soft Delete for Task with id : {task_id}")
    return repository.soft_delete(task_id, db)