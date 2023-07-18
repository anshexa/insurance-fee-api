from pydantic.main import BaseModel
from datetime import date


class CreateInsuranceFeeSchema(BaseModel):
    cargo_type: str
    date: date
    declared_value: float


class TariffSchema(BaseModel):
    cargo_type: str
    rate: str


class InsuranceFeeSchema(BaseModel):
    id: int
    cost: int


class CargoSchema(BaseModel):
    id: int
    declared_value: float
    cargo_type: str
    date: date


class CreateInsuranceFeeResponseSchema(InsuranceFeeSchema):
    cargo: CargoSchema
