from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from web.api.router import api_router


def get_app() -> FastAPI:
    app = FastAPI(
        title="UniBot",
        version='0.0.0',
        docs_url="/api/docs",
        default_response_class=UJSONResponse,
    )
    app.include_router(router=api_router, prefix="/api")
    return app
