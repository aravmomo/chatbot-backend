from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(msg: Message):
    return {"response": f"AI ne kaha: {msg.message}"}
