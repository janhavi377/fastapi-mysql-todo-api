from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas import user_schema
from app.services import user_service
from app.api.deps import get_db
from app.utils.response import success_response

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    new_user = user_service.create_user(db, user)
    return success_response(data=new_user, message="User created successfully")

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = user_service.login_user(db, form.username, form.password)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"access_token": token, "token_type": "bearer"}
