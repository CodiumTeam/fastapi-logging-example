# A FastAPI logging demo

Create a `.env` file in the root of the repo with the following contents:

```
SERVER_SENTRY_DSN=<get your sentry DSN from sentry.io>
VITE_PUBLIC_SENTRY_DSN=<get your sentry DSN from sentry.io>
```

Install dependencies and run the server:

```bash
docker compose up --build
```

Perform some requests and see the server logs

```bash
curl localhost:8000 -H "User-Id: john" -v -H "Session-Id: 1241" -H "X-Correlation-ID: 99999" 
```