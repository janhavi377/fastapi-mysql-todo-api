from sqlalchemy.orm import Session
from app.schemas.todo_schema import TodoCreate
from app.database import models

def create_todo(db: Session, todo: TodoCreate, user_id: int):
    db_todo = models.Todo(**todo.dict(), user_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_user_todos(db: Session, user_id: int):
    return db.query(models.Todo).filter(models.Todo.user_id == user_id).all()
