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
