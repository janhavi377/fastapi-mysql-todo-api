from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas import todo_schema
from app.services import todo_service
from app.api.deps import get_db, get_current_user
from app.utils.response import success_response
from app.database.models import User

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.post("/", response_model=todo_schema.TodoResponse)
def create(todo: todo_schema.TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return todo_service.create_todo(db, todo, current_user.id)

@router.get("/", response_model=List[todo_schema.TodoResponse])
def list_todos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return todo_service.get_user_todos(db, current_user.id)
