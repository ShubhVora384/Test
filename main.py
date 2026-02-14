from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

users = {}

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def create_user(user_id: int, user: User):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user_id] = user.dict()
    return {"message": "User created", "user": users[user_id]}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user.dict()
    return {"message": "User updated", "user": users[user_id]}

