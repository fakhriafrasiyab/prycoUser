from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(UserCreate):
    email: str
    password: str