from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title = "ToDOAPP")

app = FastAPI(title="My First To-Do API")

tasks = {
    1: {"title": "Learn FastAPI basics", "priority": "high", "completed": False}
}

class Task(BaseModel):
    title : str
    priority : str = "high"
    completed : bool = False

class TaskPatch(BaseModel):
    title: str | None = None
    priority: str | None = None
    completed: bool | None = None

@app.get("/tasks")
def view_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id : int):
    if task_id not in tasks:
        raise HTTPException(status_code = 404, detail = "task not found")
    return tasks[task_id]

@app.post("/tasks/{task_id}", status_code=201)
def create_task(task_id: int, task: Task):
    if task_id in tasks:
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks[task_id] = task.model_dump()
    return {"message": "Created", "task": tasks[task_id]}

@app.put("/tasks/{task_id}")
def replace_task(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task.model_dump()
    return {"message": "Replaced", "task": tasks[task_id]}

@app.patch("/tasks/{task_id}")
def update_task_partial(task_id: int, task: TaskPatch):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    updates = task.model_dump(exclude_unset=True)
    tasks[task_id].update(updates)
    return {"message": "Updated", "task": tasks[task_id]}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    removed = tasks.pop(task_id)
    return {"message": "Deleted", "task": removed}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)