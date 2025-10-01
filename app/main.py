from fastapi import FastAPI
from .database import Base, engine
from .models import Task
from .routes import router as tasks_router

app = FastAPI(title="To-Do API", version="1.0.0")
Base.metadata.create_all(bind=engine)
app.include_router(tasks_router)

@app.get("/")
def root():
    return {"message": "Welcome to the To-Do API"}
