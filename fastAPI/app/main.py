from typing import Union
from fastapi import FastAPI
from app.database.engine import engine, Base, session_local
from app.database.models import init_db
from .cache import init_redis_cache


app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
async def read_root():
    re_cache = init_redis_cache()
    value = re_cache.get('first_key')
    if value:
        value += 1
    else:
        value = 1
    re_cache.set('first_key', value)
    return {"Hello": "World", "cache_value": value}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}