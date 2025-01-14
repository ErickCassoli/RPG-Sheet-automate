from fastapi import FastAPI
from app.api.v1.routes import character_rpg_router

app = FastAPI(title="RPG Character API",
    description="API para criação e gerenciamento de personagens de RPG",
    version="1.0.0"
)

# Incluindo as rotas da API
app.include_router(character_rpg_router)

@app.get("/health-check", tags=["Health"])
async def health_check():
    return {"status": "up"}
