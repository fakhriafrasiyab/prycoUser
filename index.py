import datetime
from fastapi import Depends, FastAPI
from cachetools import TTLCache
from fastapi.routing import APIRoute
from db.index import SessionLocal, get_db
from dto.index import UserCreate, UserLogin
from sqlalchemy.orm import Session

from service.user import UserService

post_cache = TTLCache(maxsize=100, ttl=300)

# FastAPI application
app = FastAPI()


@app.post("/users/")
def signUp(user: UserCreate, db: Session = Depends(get_db)):
    userService = UserService(db)
    createdUser = userService.createUser(user);
    return {
        'timestamp':datetime.datetime.utcnow(),
        'data':createdUser.email,
        "message":"User created success"
    }


@app.post("/users/login/")
def signIn(user: UserLogin,  db: Session = Depends(get_db)):
    userService = UserService(db)
    accessToken = userService.login(user);
    return {
        'timestamp':datetime.datetime.utcnow(),
        'accessToken': accessToken
    }

