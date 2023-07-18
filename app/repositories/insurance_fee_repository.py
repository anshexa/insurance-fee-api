from app.models import InsuranceFee


async def create(cost: float, cargo_id: int) -> InsuranceFee:
    return await InsuranceFee.create(cost=cost,
                                     cargo_id=cargo_id)
