from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class usernames(BaseModel):
     sanku{
         id:1
         roll:222
     }
@app.get('/')
def index():
    return{"data":"sankeerthana"}


@app.get("/blog/{id}")
def about(id:str):
    return{"data":id}


@app.get("/blog/{id}/comments")
def comments(id:int):
    return{ "data":{'1','2'}}

@app.get("/getuser")
def getuser(id,name):
    return {
        "id":id,
        "firstname":name

    }
@app.post("/get/{user_name}")
def update(user_name:usernames):
    usernames.append(user_name)
    return{
        "username":usernames
    }

@app.get("/blog")
def index(limit):
    return {"data":f'blog list {limit}'}
@app.delete("/deletedata/{user_name}")
def delete_user(user_name):
    usernames.remove(user_name)
    return {
        "data":"succsess"
    }