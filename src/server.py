from fastapi import FastAPI

from .logging import get_logger
from .logging_middleware import logging_context, log_request_response

logger = get_logger(__name__)

app = FastAPI(middleware=[logging_context, log_request_response])


@app.get("/")
async def root():
    logger.info("Example log")
    return {"message": "Hello World"}