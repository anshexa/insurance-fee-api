from fastapi import FastAPI


def start() -> FastAPI:
    app = FastAPI(title='API для расчета стоимости страхования')

    return app
