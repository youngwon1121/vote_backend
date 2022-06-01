from pydantic import BaseModel


class Contract(BaseModel):
    name: str
    address: str
    owner_address: str

    class Config:
        orm_mode = True


class ContractInfo(BaseModel):
    id: int
    abi: str
    bytecode: str

    class Config:
        orm_mode = True
