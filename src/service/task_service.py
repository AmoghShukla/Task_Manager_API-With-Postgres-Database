from repository.task_repository import db
from utils.Task_logger import get_logger
from fastapi import HTTPException

logger = get_logger(__name__)

class Task_Service:

    def Create_Task(Payload):

        task = {
            "id" : db.Counter,
            "title" : Payload.title,
            "description" : Payload.description
        }

        db.Database[db.Counter] = task
        logger.info("Task Creation Successful!!")
        db.Counter += 1

        return task
        
    
    def Get_All_Task():
        logger.info("Fetching all Data from the Database")
        return list(db.Database.values())

    
    def Get_Task(task_id):
        task = db.Database.get(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task Not Found")
        return task
    
    def Update_Task(task_id: int, data):
        task = db.Database.get(task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task Not Found")
        logger.info(f"Updating Task with Task ID : {task_id}")

        if data.title is not None:
            task["title"] = data.title

        if data.description is not None:
            task["description"] = data.description

        return task
    
    def Delete_Task(task_id):
        if task_id not in db.Database:
            raise HTTPException(status_code=404, detail="Task Not Found")

        logger.info(f"Deleting Entry with task_id {task_id}")
        del db.Database[task_id]

        return {"message": "Task Deleted Successfully"}

