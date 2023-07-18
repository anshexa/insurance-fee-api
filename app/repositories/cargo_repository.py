from app.models import Cargo
from datetime import date


async def create(declared_value: float, cargo_type: str, date: date) -> Cargo:
    return await Cargo.create(declared_value=declared_value,
                              cargo_type=cargo_type,
                              date=date)
