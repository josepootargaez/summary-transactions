
from fastapi import Depends, FastAPI, Form, UploadFile, File , status,Response
from fastapi.middleware.cors import CORSMiddleware
from functions import CalculateTransaction

from pydantic import BaseModel
app = FastAPI(tittle='account transactions',description='Api for credit and debit transactions',version='1.0.1')
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class mail(BaseModel):
    correo:str
@app.get("/")
def index():
    return "Api for credit and debit transactions"

@app.post("/transaction", status_code=200)
async def insertTransaction(correo: mail = Depends(),file:UploadFile = File(...) , response: Response = ''):
    res = await CalculateTransaction(correo,file,response);
    try:
     if res["success"]:
        return res
    except:
        response.status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        return res




