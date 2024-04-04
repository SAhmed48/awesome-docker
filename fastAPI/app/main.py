from typing import Union
from fastapi import FastAPI
from app.database.engine import engine, Base, session_local, init_db

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def read_root():
    print(session_local())
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}