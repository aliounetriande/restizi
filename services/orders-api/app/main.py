from fastapi import FastAPI

app = FastAPI(title="Restizi - Order API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test")
def test():
    return {"service": "orders-api", "message": "Welcomee"}