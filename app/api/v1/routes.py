from fastapi import APIRouter
from app.services.pdf_service import read_pdf

router = APIRouter()

@router.get("/read-pdf", tags=["PDF"])
async def read_pdf_route():
    content = read_pdf("templates/ficha_ordem_paranormal.pdf")
    return {"message": "PDF read successfully", "content": content}
