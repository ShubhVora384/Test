# main.py
from fastapi import FastAPI, HTTPException

app = FastAPI()

# static in-memory data
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

# GET - Read
@app.get("/users")
def get_users():
    return users

# POST - Create
@app.post("/users")
def create_user(user_id: int, name: str, age: int):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user_id] = {"name": name, "age": age}
    return {"message": "User created", "user": users[user_id]}

# PUT - Update
@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = {"name": name, "age": age}
    return {"message": "User updated", "user": users[user_id]}
