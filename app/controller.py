from fastapi import APIRouter, HTTPException

from datetime import date

from app import service
from app.schemas import CreateInsuranceFeeSchema, CreateInsuranceFeeResponseSchema, CostSchema
from app.models import InsuranceFee

insurance_fee_controller = APIRouter()


@insurance_fee_controller.post(
    '/insurance-fees',
    response_model=CreateInsuranceFeeResponseSchema,
    tags=['Страховые взносы'],  # для документации swagger
    summary='Создать страховой взнос')  # для документации swagger
async def post(data: CreateInsuranceFeeSchema) -> InsuranceFee:
    return await service.create_cargo_and_insurance_fee(data)


@insurance_fee_controller.get(
    '/insurance-fees',
    response_model=CostSchema,
    tags=['Страховые взносы'],  # для документации swagger
    summary='Получить стоимость страхового взноса')  # для документации swagger
async def get(cargo_type: str, declared_value: str, date: date) -> dict:
    cost = await service.get_cost(cargo_type, declared_value, date)
    if cost:
        return {'cost': cost}
    else:
        raise HTTPException(status_code=404, detail="Страховой взнос не найден")
