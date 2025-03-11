from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str

@app.get("/")
async def root():
    return {"message": "This is root"}

@app.get("/patrick")
async def patrick_is_here():
    return {"message": "No this is Patrick"}

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

@app.post("/user")
async def create_user(user:User):
    return {"Got user": user.name}
