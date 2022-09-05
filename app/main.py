from typing import Union

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None, c: Union[int, None] = 1):
    return {"item_id": item_id, "q": q, "c": c}


@app.get("/users/me")
async def read_user_me():
    x = list(("a", "b", "c"))

    return {"user_id": "the current user", "list": x}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
