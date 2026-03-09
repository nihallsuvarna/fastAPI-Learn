from fastapi import FastAPI
from .database import engine, Base
from .models import Note
from .routers import notes

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(notes.router)


@app.get("/")
def read_root():
    return {"Message": "Welcome to the Notes API"}
