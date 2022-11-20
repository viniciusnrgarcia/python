"""
https://fastapi.tiangolo.com/
"""

from fastapi import FastAPI
from typing import Union
import uvicorn
import os
from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


list = []

app = FastAPI()


@app.get("/healthcheck/")
def healthcheck():
    return 'Health - OK'


@app.get("/hello")
async def read_root():
    return {"Hello": "World"}


@app.get("/")
async def read_root():
    return list


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    list.append(item)
    return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))
