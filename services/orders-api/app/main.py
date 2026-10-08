from fastapi import FastAPI

app = FastAPI(title="Restizi - Orders API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"service": "orders-api", "app": "Restizi", "message": "Bienvenue sur Restizi"}