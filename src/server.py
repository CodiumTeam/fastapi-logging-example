from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .logging import get_logger
from .logging_middleware import logging_context, log_request_response

logger = get_logger(__name__)

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