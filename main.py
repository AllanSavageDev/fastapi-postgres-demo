from fastapi import FastAPI
import asyncpg

app = FastAPI()

DATABASE_URL = "postgresql://postgres:secret@localhost:5432/postgres"


@app.on_event("startup")
async def startup():
    app.state.db = await asyncpg.connect(DATABASE_URL)
    
    # Create table if it doesn't exist
    await app.state.db.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)









@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close()



@app.get("/")
async def read_root():
    result = await app.state.db.fetchrow("SELECT * FROM messages LIMIT 1")
    return {"id": result["id"], "content": result["content"]}




