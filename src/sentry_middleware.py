from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware

from sentry_sdk import set_tag, set_user


class SentryMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        set_tag("transaction_id", request.headers.get("X-Correlation-ID"))
        set_tag("session_id", request.headers.get("Session-Id"))
        set_user({'name': request.headers.get("User-Id")})

        return await call_next(request)


sentry_middleware = Middleware(SentryMiddleware)