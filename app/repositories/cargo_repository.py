from datetime import date

from app.models import Cargo


async def create(declared_value: float, cargo_type: str, date: date) -> Cargo:
    return await Cargo.create(declared_value=declared_value,
                              cargo_type=cargo_type,
                              date=date)


async def get(cargo_type: str, declared_value: str, date: date) -> Cargo | None:
    return await Cargo.filter(declared_value=declared_value,
                              cargo_type=cargo_type,
                              date=date).first()


async def get_related(cargo: Cargo) -> Cargo:
    await cargo.fetch_related('insurance_fee')
    return cargo
