from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

# Models
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None

users = {}
current_id = 1


@app.get("/users")
def get_users():
    return [
        {"id": user_id, **data}
        for user_id, data in users.items()
    ]


@app.post("/users")
def create_user(user: UserCreate):
    global current_id

    users[current_id] = user.dict()
    response = {"id": current_id, **users[current_id]}
    current_id += 1

    return response


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    stored_user = users[user_id]

    update_data = user.dict(exclude_unset=True)
    stored_user.update(update_data)

    return {"id": user_id, **stored_user}
