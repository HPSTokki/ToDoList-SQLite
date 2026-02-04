from fastapi import FastAPI, Depends, HTTPException, Query
from dotenv import load_dotenv

from typing import Annotated, List
from sqlmodel import Field, Session, create_engine, select, SQLModel

import os

# This one of course initializes the FastAPI environment
app = FastAPI()

# Loading the env vars in the ".env" file in the root
load_dotenv()

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task_name: str = Field(index=True)
    isCompleted: bool = Field(default=False)

# Below is the Database URL, put it in a ".env" file in the root src
supabase_url = os.getenv("DATABASE_URL")

connect_args = {"check_same_thread": False} # Ignore this since this is for SQLite/LocalDB, HOWEVER!!!!! USE THIS WHEN YOU ARE USING SQLITE DB

engine = create_engine(supabase_url)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@app.get("/task")
async def getTasks(session: SessionDep) -> List[Task]:
    statement = select(Task)
    session.get
    tasks = session.exec(statement).all()
    return tasks

@app.post("/task")
async def addTasks(session: SessionDep, task: Task):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@app.delete("/task/{task_id}")
async def delTask(session: SessionDep, task_id: int):
    res = session.get(Task, task_id)
    if not res:
        raise HTTPException(status_code=404, detail="Task Not Found")
    session.delete(res)
    session.commit()
    return {
        "ok": True
    }

@app.put("/task/{task_id}")
async def updateTask(session: SessionDep, task_id: int, task_details: Task):
    res = session.get(Task, task_id)
    if not res:
        raise HTTPException(status_code=404, detail="Task Not Found")
    
    res.isCompleted = task_details.isCompleted

    session.add(res)
    session.commit()
    return {
        "ok": True
    }