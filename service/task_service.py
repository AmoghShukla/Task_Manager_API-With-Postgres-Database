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
        logger.info(f"Getching the Task with Task Id : {task_id}")
        return db.Database[task_id]
    
    def Update_Task(task_id: int, data):
        if task_id in db.Database:
            task = db.Database.get(task_id)
            logger.info(f"Updating Task with Task ID : {task_id}")
            if not task:
                return None

            if data.title is not None:
                task["title"] = data.title
            if data.description is not None:
                task["description"] = data.description
            return task
        else:
            raise HTTPException(status_code=404, detail="Task Not Found")
    
    def Delete_Task(task_id):
        if task_id in db.Database:
            logger.info(f"Deleting Entry with taks_id {task_id}")
            del db.Database[task_id]
            return "Task Deleted Successfully"
        else:
            return HTTPException(status_code=404, detail="Task Not Found")

