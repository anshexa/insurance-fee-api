from app.models import InsuranceFee


async def create(cost: float, cargo_id: int) -> InsuranceFee:
    insurance_fee = await InsuranceFee.create(cost=cost,
                                              cargo_id=cargo_id)
    await insurance_fee.fetch_related('cargo')
    return insurance_fee
