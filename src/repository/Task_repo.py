from src.models.task_model import Task
# from src.schemas.task_schema import Status


def _to_dict(payload, exclude_unset: bool = False):
	if hasattr(payload, "model_dump"):
		return payload.model_dump(exclude_unset=exclude_unset)
	return payload


def _task_to_response(task: Task):
	return {
		"id": task.id,
		"title": task.title,
		"description": task.description,
	}


def create(data, db):
		task_data = _to_dict(data)
		task = Task(
			title=task_data["title"],
			description=task_data.get("description"),
		)
		db.add(task)
		db.commit()
		db.refresh(task)
		return task
		# return _task_to_response(task)
	


def get_all(db, completed: bool = None):
	try:
		query = db.query(Task)
		if completed is not None:
			query = query.filter(Task.completed == completed)
		tasks = query.all()
		return [_task_to_response(task) for task in tasks]
	finally:
		db.close()


def get_by_id(task_id: int, db):
	try:
		task = db.query(Task).filter(Task.id == task_id).first()
		if not task or task("is_active") == False:
			return None
		return _task_to_response(task)
	finally:
		db.close()


def update(task_id: int, data, db):
	try:
		task = db.query(Task).filter(Task.id == task_id).first()
		if not task:
			return None

		update_data = _to_dict(data, exclude_unset=True)
		for field in ("title", "description", "completed"):
			if field in update_data:
				setattr(task, field, update_data[field])

		db.commit()
		db.refresh(task)
		return _task_to_response(task)
	finally:
		db.close()

def soft_delete(task_id: int, db):
	try:
		task = db.query(Task).filter(Task.id == task_id).first()
		if not task:
			return False

		task.is_active = False
		db.commit()
		return True
	finally:
		db.close()

def delete(task_id: int, db):
	try:
		task = db.query(Task).filter(Task.id == task_id).first()
		if not task:
			return False

		db.delete(task)
		db.commit()
		return True
	finally:
		db.close()
