from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import crud
import models
import schemas
from database import SessionLocal, engine

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/contracts/", response_model=List[schemas.Contract])
def read_contracts(owner_address: str, db: Session = Depends(get_db)):
    return crud.get_contracts_by_owner_address(db, owner_address=owner_address)


@app.post("/contracts/", response_model=schemas.Contract)
def read_item(contracts: schemas.Contract, db: Session = Depends(get_db)):
    return crud.create_contract(db, item=contracts)

@app.get("/contract_info/", response_model=schemas.ContractInfo)
def read_contracts(db: Session = Depends(get_db)):
    return crud.get_contract_info(db)

@app.post("/contract_info/", response_model=schemas.ContractInfo)
def read_item(contract_info: schemas.ContractInfo, db: Session = Depends(get_db)):
    return crud.create_contract_info(db, item=contract_info)


from web3 import Web3
@app.get("/test/")
def read_contracts(db: Session = Depends(get_db)):
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
    print(w3.isConnected())
    return {"hello":"!234"}
