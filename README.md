# FastAPI + Postgres Demo

A simple backend application built with FastAPI and PostgreSQL, running inside Docker Compose.

## Features

- FastAPI server for RESTful APIs
- PostgreSQL database with Dockerized environment
- Docker Compose orchestration
- Full CRUD operations on `messages` table
- Auto-generated API documentation via Swagger UI
- Health Check: `http://localhost:8000/health`


## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/AllanSavageDev/fastapi-postgres-demo.git
   cd fastapi-postgres-demo


# FastAPI + Postgres Demo - Developer Notes

## Initial Setup
- Create and activate Python venv
- Install FastAPI and Uvicorn
- Install asyncpg
- Create main.py
- Set up Dockerfile and docker-compose.yml

## Key Commands
- Start app: `docker compose up --build`
- Stop app: `docker compose down`
- Test health: `http://localhost:8000/health`
- Test GET messages: `http://localhost:8000/messages`
- POST message (curl example):
  ```bash
  curl -X POST http://localhost:8000/messages \
    -H "Content-Type: application/json" \
    -d '{"content": "Test message"}'
