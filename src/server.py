import os

import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .logging import get_logger
from .logging_middleware import logging_context, log_request_response

logger = get_logger(__name__)

sentry_sdk.init(
    dsn=os.environ["SERVER_SENTRY_DSN"],
    traces_sample_rate=1.0,
)

app = FastAPI(middleware=[logging_context, log_request_response])
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    logger.info("Example log")
    return {"message": "Hello World"}


@app.get("/error")
async def trigger_error():
    division_by_zero = 1 / 0
    return {"message": "We divided something"}