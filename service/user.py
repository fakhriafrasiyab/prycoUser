from fastapi import Depends, HTTPException
from dto.index import UserCreate, UserLogin
from model.user import User
from utils.index import hash_password, verify_password
from security.index import create_token, verify_token
from repository.user import UserRepository
from sqlalchemy.orm import Session


class UserService:

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def createUser(self, user:UserCreate):
        existing_email = self.user_repository.getUserByEmail(user.email)
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")

        user.password = hash_password(user.password)

        createdUser:User = self.user_repository.createUser(user)

        return createdUser

    def login(self, user:UserLogin):
        findUser:User = self.user_repository.getUserByEmail(user.email)

        if not findUser:
            raise HTTPException(status_code=400, detail="User not found")
        
        comparePassword = verify_password(user.password, findUser.password)

        if not comparePassword:
            raise HTTPException(status_code=400, detail="Email or password is wrong")
        
        return create_token(findUser.email)