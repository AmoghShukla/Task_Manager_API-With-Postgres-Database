# Models for the postgres database
from sqlalchemy import Boolean, Column, Integer, String

from src.database.base import Base


class Task(Base):
	__tablename__ = "tasks"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String(255))
	description = Column(String)
	completed = Column(Boolean, default=False)
	is_active = Column(Boolean, default=True)