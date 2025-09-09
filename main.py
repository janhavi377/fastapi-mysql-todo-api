# from fastapi import FastAPI
# from app.database.connection import Base, engine
# from app.api import auth_routes, todo_routes

# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="User & Todo API")

# app.include_router(auth_routes.router)
# app.include_router(todo_routes.router)


from fastapi import FastAPI

from app.api import auth_routes, todo_routes  # adjust based on your structure

app = FastAPI(title="User & Todo API")

# Register routers
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(todo_routes.router, prefix="/todos", tags=["Todos"])

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the User & Todo Management API 🚀"}
