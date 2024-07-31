from fastapi import FastAPI,BackgroundTasks,Path
from pydantic import BaseModel
import asyncio

app=FastAPI()

class Employee(BaseModel):
    name:str
    role:str
employee={
    1:{
        "name":"sanku",
        "role":"tester"
     }
}
async def task_a():
    await asyncio.sleep(2)
    print("task a completed")
async def task_b():
     await asyncio.sleep(3)
     print("task b completed")
@app.get("/run")
async def run_tasks(bg_task: BackgroundTasks):
    bg_task.add_task(task_a)
    bg_task.add_task(task_b)
    return {"message": "Tasks scheduled"}

@app.get("/test/{employe_id}")
def test(employe_id:int =  Path(description = "ID is required", gt=0 , le=3)):
    if employe_id in employee:
        return employee[employe_id]
    return {"Data":"Not found"}


