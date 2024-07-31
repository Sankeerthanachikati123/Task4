from typing import Annotated
from fastapi import Depends,FastAPI
from fastapi.security import HTTPBasic,HTTPBasicCredentials


app=FastAPI()

security=HTTPBasic()

@app.get("/user/me")
def read(credentials:Annotated[HTTPBasicCredentials,Depends(security)]):
     return{"username":credentials.username,"password":credentials.password}