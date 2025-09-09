from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.database import models
from app.core import security

def create_user(db: Session, user: UserCreate):
    hashed_pw = security.get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not security.verify_password(password, user.password):
        return None
    token = security.create_access_token({"sub": str(user.id)})
    return token
