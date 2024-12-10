from fastapi import FastAPI
from app.api.v1.routes import router

app = FastAPI(title="RPG Sheet Automate", version="1.0.0")

# Incluindo as rotas da API
app.include_router(router)

@app.get("/health-check", tags=["Health"])
async def health_check():
    return {"status": "up"}
