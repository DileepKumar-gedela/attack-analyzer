from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import User
from app.auth import hash_password, verify_password, create_token

router = APIRouter()


@router.post("/register")
def register(username: str, password: str,
             db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.username == username
    ).first()

    if user:
        raise HTTPException(400, "Username exists")

    new_user = User(
        username=username,
        password=hash_password(password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created"}


@router.post("/login")
def login(username: str, password: str,
          db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user or not verify_password(
            password, user.password):
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"sub": username})

    return {"access_token": token}
