
import csv
from fastapi import FastAPI, UploadFile, File
app = FastAPI(tittle='account transactions',description='Api for credit and debit transactions',version='1.0.1')

@app.get("/")
def index():
    return "Api for credit and debit transactions"

@app.post("/transaction")
async def insertTransaction(file:UploadFile = File(...)):
#    csvreader = csv.reader(file)
#    header = next(csvreader)
#    print(header)
   return {"file_name":file.filename}