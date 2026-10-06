from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.controller import get_api_router

STATIC_DIR = Path(__file__).parent / "static"

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(get_api_router())
    app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")

    return app

if __name__ == '__main__':
    uvicorn.run(
        app="src.app:create_app",
        port=8080,
    )