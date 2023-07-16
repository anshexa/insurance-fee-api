from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import os


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

    return app


def get_db_uri(user, password, host, port, db):
    return f"postgres://{user}:{password}@{host}:{port}/{db}"
