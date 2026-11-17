from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
import models
import schemas  # Импортируем наши схемы

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend Service", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Привет! Бэкенд на Python и FastAPI успешно запущен!"}

# Используем Pydantic-схему UserCreate для валидации тела запроса
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Обращаемся к полям через точку: user.name и user.email
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user  # FastAPI сам упакует объект в схему UserResponse


@app.get("/users/", response_model=list[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user
