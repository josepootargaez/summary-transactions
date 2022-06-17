# summary-transactions
    Summary Transactions its an api that allow read to csv file and send mail with account transactions

## Technical specifications of the environment

* **Python** - `v3.0`
* **uvicorn** - `v0.17.6`
* **fastapi** - `v0.78.0`
* **docker** - `v20.10.16`


## Installation
 clone the repository

### Stori Transaction
git clone https://github.com/josepootargaez/summary-transactions.git  
cd summary-transactions
 ### run the next comands to active the docker container and deploy api

    docker build -t summary-transactions .

    docker run -it -p 8000:8000 -v /app summary-transactions

### show api 
http://localhost:8000/docs

### install front aplication in
https://github.com/josepootargaez/summary-transactions-front.git

## optional
 ### run without docker and run in local 
    pip install -r requirements.txt
    uvicorn main:app --reload