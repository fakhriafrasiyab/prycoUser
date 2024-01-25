from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, select, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from cachetools import TTLCache

# Create SQLAlchemy models
Base = declarative_base()
metadata = MetaData()


# Define the database connection string
DATABASE_URL = "postgresql://postgres:admin@localhost/postgres"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a SessionLocal class to handle the database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get the current user
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Token verification function
def verify_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Your token verification logic here (decode token, check database, etc.)
    return True

# Pydantic schemas
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(UserCreate):
    pass

class PostCreate(BaseModel):
    text: str

class Post(BaseModel):
    id: int
    text: str

# FastAPI application
app = FastAPI()

# In-memory cache for posts
post_cache = TTLCache(maxsize=100, ttl=300)

# Signup endpoint
@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Your signup logic here (create user in the database, generate token, etc.)
    return {"token": "some_generated_token"}

# Login endpoint
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Your login logic here (validate credentials, generate token, etc.)
    return {"token": "some_generated_token"}

# AddPost endpoint
@app.post("/addPost")
def add_post(post: PostCreate, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    # Your add post logic here (save post in memory, return postID, etc.)
    return {"postID": "some_generated_post_id"}

# GetPosts endpoint with response caching
@app.get("/getPosts")
def get_posts(token: str = Depends(verify_token), db: Session = Depends(get_db)):
    # Check cache first
    if token in post_cache:
        return post_cache[token]

    # Your get posts logic here (retrieve posts from the database, etc.)
    posts = [{"id": 1, "text": "Post 1"}, {"id": 2, "text": "Post 2"}]

    # Cache the response
    post_cache[token] = posts
    return posts

# DeletePost endpoint
@app.delete("/deletePost")
def delete_post(post_id: int, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    # Your delete post logic here (delete post from memory, database, etc.)
    return {"message": "Post deleted successfully"}