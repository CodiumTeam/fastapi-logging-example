import logging

from starlette_context import context


class FastApiLoggingFilter(logging.Filter):
    def filter(self, record):
        record.context = f"session:{self._get_session_id()} user:{self._get_user_id()} traceId:{self._get_trace_id()}"
        return True

    def _get_session_id(self):
        return context.get("Session-Id")

    def _get_user_id(self):
        return context.get("User-Id")

    def _get_trace_id(self):
        return context.get("X-Correlation-ID")

