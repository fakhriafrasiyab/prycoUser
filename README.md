# FastAPI Application

This is a simple FastAPI application demonstrating user registration, authentication, and post management functionalities. The application uses PostgreSQL as the database and Pydantic for data validation.

## Features

1. User registration (`/signup`) and authentication (`/login`) endpoints.
2. Token-based authentication for protected endpoints (`/addPost`, `/getPosts`, `/deletePost`).
3. Ability to add, retrieve, and delete user posts (`/addPost`, `/getPosts`, `/deletePost`).
4. Input and output data validation using Pydantic schemas.
5. Response caching for the `getPosts` endpoint using `cachetools`.

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Pydantic
- Cachetools
- PostgreSQL database

## Installation

1. Install the required packages:

   ```bash
   pip install fastapi[all] python-jose[pyjwt] sqlalchemy cachetools psycopg2
