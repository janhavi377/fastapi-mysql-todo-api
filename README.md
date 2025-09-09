FastAPI + MySQL Todo API
A simple User & Todo Management API built with FastAPI and MySQL, featuring JWT authentication, clean architecture, and CRUD operations.

📌 Features
🔐 Authentication

POST /auth/signup → Register a new user
POST /auth/login → Login and receive JWT

✅ Todo Management (JWT Protected)

POST /todos/ → Create a new todo
GET /todos/ → List user’s todos (supports status filter & pagination)
GET /todos/{id} → Fetch a single todo (only owner can access)
PUT /todos/{id} → Update a todo
DELETE /todos/{id} → Delete a todo

🛠 Tech Stack

FastAPI – Web framework
MySQL – Database
SQLAlchemy – ORM
Alembic – Database migrations
Pydantic – Data validation
JWT – Authenticatio

📂 Project Structure
app/
│── main.py                # FastAPI entrypoint
│── core/
│   ├── config.py          # Settings (DB, JWT secret, etc.)
│   ├── security.py        # JWT utils, password hashing
│
│── database/
│   ├── connection.py      # DB connection
│   ├── models.py          # SQLAlchemy models
│
│── schemas/
│   ├── user_schema.py     # Pydantic models for User
│   ├── todo_schema.py     # Pydantic models for Todo
│
│── api/
│   ├── deps.py            # Dependencies
│   ├── auth_routes.py     # Auth endpoints
│   ├── todo_routes.py     # Todo endpoints
│
│── services/
│   ├── user_service.py    # User business logic
│   ├── todo_service.py    # Todo business logic
│
│── utils/
│   ├── response.py        # Response formatting
│   ├── exceptions.py      # Custom exceptions
│
│── __init__.py


📖 API Docs

Swagger UI → http://127.0.0.1:8000/docs#/Auth/signup_auth_auth_signup_post

ReDoc → create_todos__post
