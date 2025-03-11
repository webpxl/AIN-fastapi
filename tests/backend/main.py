from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

app = FastAPI()

# Don't touch this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])

class TodoItem(BaseModel):
    id: int
    title: str
    description: str = ""

todo_list: List[TodoItem] = []

def get_db():
    return todo_list

@app.get("/todos", response_model=List[TodoItem])
def read_items(db: Annotated[List[TodoItem], Depends(get_db)]):
    return db

@app.get("/todos/{item_id}", response_model=TodoItem)
def read_item(item_id: int, db: Annotated[List[TodoItem], Depends(get_db)]):
    print("Before fetch item")
    print(db)
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/todos", response_model=TodoItem)
def add_item(item: TodoItem, db: Annotated[List[TodoItem], Depends(get_db)]):
    db.append(item)
    return item

@app.delete("/todos/{item_id}")
def delete_item(item_id: int, db: Annotated[List[TodoItem], Depends(get_db)]):
    item = next((item for item in db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.remove(item)
    return {"message": "Item deleted"}

@app.get("/search", response_model=List[TodoItem])
def search_item(keyword: str, db: Annotated[List[TodoItem], Depends(get_db)]):
    return [item for item in db if keyword.lower() in item.title.lower() or keyword.lower() in item.description.lower()]
