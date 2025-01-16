from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from web.api.router import api_router


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="UniBot",
        version='0.0.0',
        docs_url="/api/docs",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    # register_startup_event(app)
    # register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")

    return app
