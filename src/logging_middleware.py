from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette_context.middleware import RawContextMiddleware
from starlette_context.plugins import Plugin

from .logging import get_logger

logger = get_logger(__name__)


class UserIdPlugin(Plugin):
    key = "User-Id"


class SessionIdPlugin(Plugin):
    key = "Session-Id"


class CorrelationIdPlugin(Plugin):
    key = "X-Correlation-ID"


logging_context = Middleware(
    RawContextMiddleware,
    plugins=(
        UserIdPlugin(),
        SessionIdPlugin(),
        CorrelationIdPlugin()
    )
)


class LogRequestResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f" --> {request.method} {request.url.path}")
        response = await call_next(request)
        logger.info(f" <-- {response.status_code}")

        return response


log_request_response = Middleware(LogRequestResponseMiddleware)
