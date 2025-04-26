from fastapi import FastAPI
import asyncpg
import asyncio
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL = "postgresql://postgres:secret@db:5432/postgres"

class MessageIn(BaseModel):
    content: str

@app.on_event("startup")
async def startup():
    for attempt in range(10):
        try:
            app.state.db = await asyncpg.connect(DATABASE_URL)
            break
        except Exception as e:
            print(f"Database connection failed (attempt {attempt + 1}), retrying...")
            await asyncio.sleep(2)

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close()

@app.get("/")
async def read_root():
    result = await app.state.db.fetchval("SELECT 'Hello, Allan Savage!'")
    return {"message": result}

@app.post("/messages")
async def create_message(message: MessageIn):
    query = "INSERT INTO messages (content) VALUES ($1) RETURNING id;"
    new_id = await app.state.db.fetchval(query, message.content)
    return {"id": new_id, "content": message.content}

@app.get("/messages")
async def get_messages():
    query = "SELECT id, content FROM messages ORDER BY id;"
    rows = await app.state.db.fetch(query)
    messages = [{"id": row["id"], "content": row["content"]} for row in rows]
    return messages

@app.get("/health")
async def health_check():
    return {"status": "ok"}
