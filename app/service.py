from datetime import date

from app.repositories import insurance_fee_repository, cargo_repository
from app.repositories import tariff_repository
from app.schemas import CreateInsuranceFeeSchema
from app.models import InsuranceFee


async def create_cargo_and_insurance_fee(data: CreateInsuranceFeeSchema) -> InsuranceFee:
    declared_value = data.declared_value
    cargo_type = data.cargo_type
    date = data.date

    cost = await calculate_cost(cargo_type, date, declared_value)
    cargo = await cargo_repository.create(declared_value, cargo_type, date)
    insurance_fee = await insurance_fee_repository.create(cost, cargo.id)
    return insurance_fee


async def calculate_cost(cargo_type: str, date: date, declared_value: float) -> float:
    tariff = await tariff_repository.get(date, cargo_type)
    cost = declared_value * float(tariff['rate'])
    return cost


async def get_cost(cargo_type: str, declared_value: str, date: date) -> float | None:
    cargo = await cargo_repository.get(cargo_type, declared_value, date)
    cost = None
    if cargo:
        cargo = await cargo_repository.get_related(cargo)
        cost = cargo.insurance_fee.cost
    return cost
