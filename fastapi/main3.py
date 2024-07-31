from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class student(BaseModel):
    title:str
    body:str


@app.post("/blog")
def create(request:student):
    return request
   # return {"data":f"blog is created with {request.title}"}
@app.delete("/delete_data/{title}")
def blog(title:student):
    student.remove(title)
    return{
        "data":"success"
    }


#@app.put("/get/{id}")
#def update(id:int,post:Post):