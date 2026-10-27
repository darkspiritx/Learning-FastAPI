
import logging
import psycopg
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routes import router

app = FastAPI(title="Student Management API")
app.include_router(router)

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


@app.exception_handler(psycopg.Error)
async def database_error_handler(
    request: Request,
    exc: psycopg.Error,
):
    logger.error(
        "Database error on %s %s",
        request.method,
        request.url.path,
        exc_info=(type(exc), exc, exc.__traceback__),
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "A database error occurred. Please try again later."
        },
    )
