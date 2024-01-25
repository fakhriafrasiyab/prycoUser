# from fastapi import Depends
# from db.index import Base, engine, SessionLocal
# from sqlalchemy.orm import Session

# from dto.index import UserCreate, UserLogin
# from model.user import User


# Base.metadata.create_all(bind=engine)

# async def createUser(user:UserCreate, db: Session = Depends(SessionLocal)):
    
#     createdUser = User(email=user.email, password=user.password)

#     await db.add(createdUser)
#     await db.commit()
#     await db.refresh(createdUser)

#     return createdUser

# async def getUser(user:UserLogin, db: Session = Depends(SessionLocal)):
#     return await db.query(User).filter(User.email == user.email).first()


from sqlalchemy.orm import Session
from dto.index import UserCreate
from model.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def createUser(self, user:UserCreate):
        new_user = User(email=user.email, password=user.password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def getUserByEmail(self, email: str):
        return self.db.query(User).where(User.email == email).first()