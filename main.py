# Description: This file contains the FastAPI code for the web server.


from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# Mount the static files from the 'static' folder
app.mount("/static", StaticFiles(directory="static"), name="static")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Serve the index.html file
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_offer": item.is_offer}
    

# to run the server, use the command: uvicorn main:app --reload
# default port is: 8000