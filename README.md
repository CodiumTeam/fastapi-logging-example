# A FastAPI logging demo

Install dependencies and run the server:

```bash
pipenv install
pipenv run uvicorn src.server:app --reload --no-access-log
```

Perform some requests and see the server logs

```bash
curl localhost:8000 -H "User-Id: john" -v -H "Session-Id: 1241" -H "X-Correlation-ID: 99999" 
```