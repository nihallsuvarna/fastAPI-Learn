from pydantic import BaseModel
from fastapi import FastAPI, Path


class Todo(BaseModel):
    title: str
    completed: bool
    id: int


app = FastAPI()
todos = {}


# Home
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Todos
@app.get("/todos")
def get_todos():
    return todos


# Create Todo
@app.post("/todos")
def create_todo(todo: Todo):
    todos[todo.id] = todo
    return todos


# Get a Todo
@app.get("/todos/{todo_id}")
def get_todo(todo_id: str = Path(..., title="The ID of the todo to get")):
    return todos[str(todo_id)]


# Update a Todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int = Path(..., title="The ID of the todo to update")):
    return todos[str(todo_id)]


# Delete a Todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int = Path(..., title="The ID of the todo to delete")):
    todos.pop(todo_id)
    return todos
