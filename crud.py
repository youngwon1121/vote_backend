from sqlalchemy.orm import Session

import schemas
import models


def get_contracts_by_owner_address(db: Session, owner_address: str):
    return db.query(models.Contract).filter(models.Contract.owner_address == owner_address).all()


def create_contract(db: Session, item: schemas.Contract):
    db_item = models.Contract(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_contract_info(db: Session):
    return db.query(models.ContractInfo).order_by(models.ContractInfo.id.desc()).first()


def create_contract_info(db: Session, item: schemas.ContractInfo):
    db_item = models.ContractInfo(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
