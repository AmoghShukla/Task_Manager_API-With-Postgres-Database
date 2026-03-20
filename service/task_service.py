from repository.task_repository import db
from utils.Task_logger import logger

logger = get_lo

class Task_Service:

    def Create_Task(Payload):

        task = {
            "id" : db.Counter,
            "title" : Payload.title,
            "description" : Payload.description
        }

        db.Database[db.Counter] = task
        
    
    def Get_All_Task():
        return repository
    
    def Get_Task(task_id):
        return repository
    
    def Update_Task(task_id):
        return repository
    
    def Delete_Task(task_id):
        return repository