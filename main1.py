from fastapi  import FastAPI
app=FastAPI()
@app.get("/get")
def get(id,name):

    return[{
        "id":id,
        "firstname":name
    }]


from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Employee(BaseModel):
    name: str
    role: str


employee = {
    1: {
        "name": "sanku",
        "role": "tester"
    }
}


@app.put("/update/{id}")
def update(employe_id: int, employee: Employee):
    if employe_id not in employee:
        return {"Employe": "NOt exsists"}
    employee[employe_id] = employe
