from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model
class Message(BaseModel):
    text: str

# In-memory store
saved_message = ""

# POST method
@app.post("/save")
def save_message(msg: Message):
    global saved_message
    saved_message = msg.text
    return {"message": "Message saved!"}

# GET method
@app.get("/read")
def read_message():
    return {"saved_message": saved_message}
