from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class Contract(Base):
    __tablename__ = "contracts"

    address = Column(String, primary_key=True, index=True)
    name = Column(String)
    owner_address = Column(String)


class ContractInfo(Base):
    __tablename__ = "contract_info"

    id = Column(Integer, primary_key=True, index=True)
    abi = Column(String)
    bytecode = Column(String)
