from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import os

from app.controller import insurance_fee_controller


def start() -> FastAPI:
    app = FastAPI(title='API для расчета стоимости страхования')

    # регистрируем бд
    register_tortoise(
        app,
        db_url=get_db_uri(
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
            host=os.environ['POSTGRES_HOST'],
            port=os.environ['POSTGRES_PORT'],
            db=os.environ['POSTGRES_DB']
        ),
        modules={"models": ["app.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    register_controller(app=app)

    return app


def get_db_uri(user, password, host, port, db) -> str:
    return f"postgres://{user}:{password}@{host}:{port}/{db}"


def register_controller(app: FastAPI) -> None:
    app.include_router(insurance_fee_controller)
