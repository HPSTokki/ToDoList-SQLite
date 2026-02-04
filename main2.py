from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from typing import Annotated, List
from sqlmodel import Field, Session, create_engine, select, SQLModel, insert, delete

import os

# This one of course initializes the FastAPI environment
app = FastAPI()

app.add_middleware(
    CORSMiddleware
)

# Loading the env vars in the ".env" file in the root | DO IGNORE IF YOU RUN THIS
load_dotenv()

# Creates a user model class for easier database CRUD mechanics
class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task_name: str = Field(index=True)
    isCompleted: bool = Field(default=False)

# This one makes the databse by the root src of project
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args)


# Function below spins up the database -> auto generate/migrate said class model above to the local db
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# Reusable SessionDep for CRUD

SessionDep = Annotated[Session, Depends(get_session)]

# localhost:8000 on browser
@app.get("/")
async def getHome():
    return {
        "message": "Hello World!"
    }

@app.get("/task")
async def getTasks(session: SessionDep) -> List[Task]:
    stmt = select(Task)
    task = session.exec(stmt).all()
    return task

@app.post("/task")
async def addTask(session: SessionDep, task: Task):
    session.add(task)
    session.commit()
    session.refresh(task)
    return {
        "ok": True
    }

@app.delete("/task/{task_id}")
async def delTask(session: SessionDep, task_id: int):
    delOneTask = delete(Task).where(task_id == task_id)
    res = session.exec(delOneTask).all()
    return {
        "ok": True
    }



