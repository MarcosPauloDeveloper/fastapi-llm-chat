from fastapi import FastAPI
from app.api.routers import chat
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(chat.router)
    return app


app = create_app()
