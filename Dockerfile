FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pipenv sync --system
COPY src/ ./src/

CMD ["uvicorn", "src.server:app", "--no-access-log", "--host=0.0.0.0"]