from fastapi import APIRouter

from app import service
from app.schemas import CreateInsuranceFeeSchema, CreateInsuranceFeeResponseSchema
from app.models import InsuranceFee

insurance_fee_controller = APIRouter()


@insurance_fee_controller.post(
    '/insurance-fees',
    response_model=CreateInsuranceFeeResponseSchema,
    tags=['Страховые взносы'],  # для документации swagger
    summary='Создать страховой взнос')  # для документации swagger
async def post(data: CreateInsuranceFeeSchema) -> InsuranceFee:
    return await service.create_cargo_and_insurance_fee(data)
