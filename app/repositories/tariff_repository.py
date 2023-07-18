import json
from datetime import date

from app.schemas import TariffSchema


async def get(date: date, cargo_type: str) -> TariffSchema:
    text = await read_from_file('tariff.json')

    tariffs = text[date.strftime("%Y-%m-%d")]
    tariff = {}
    for elem in tariffs:
        if cargo_type in elem.values():
            tariff = elem
            break
    return tariff


async def read_from_file(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as file:
        text = json.load(file)
        return text
