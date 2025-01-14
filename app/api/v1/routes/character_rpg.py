from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.schemas.character_schema import Character
from app.services.pdf_service import preencher_ficha
from typing import List
import uuid
from pathlib import Path

router = APIRouter()

# Banco de dados simulado
characters_db = []


# Criar personagem e preencher ficha
@router.post("/", response_model=Character, status_code=201)
def create_character(character: Character):
    # Gera um ID único
    new_character = character.model_dump()
    new_character["id"] = str(uuid.uuid4())
    characters_db.append(new_character)

    # Preenche o PDF
    preencher_ficha(new_character)

    return new_character


# Listar personagens
@router.get("/", response_model=List[Character])
def list_characters():
    return characters_db


# Baixar ficha em PDF
@router.get("/{nome_personagem}/download")
def download_character_sheet(nome_personagem: str):
    # Caminho do PDF preenchido
    output_path = Path(__file__).parent.parent.parent.parent / "outputs" / f"{nome_personagem}_Ficha.pdf"

    # Verifica se o arquivo existe
    if not output_path.exists():
        raise HTTPException(status_code=404, detail="Ficha não encontrada.")

    # Retorna o arquivo para download
    return FileResponse(
        path=str(output_path),
        filename=f"{nome_personagem}_Ficha.pdf",
        media_type="application/pdf"
    )
