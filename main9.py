from fastapi import FastAPI

app=FastAPI()
@app.get("/get")
def get():
    return{"data":"sanku"}
@app.get("/get")
def get(name,id):
     return{
         "data":name
         "identity":id
     }