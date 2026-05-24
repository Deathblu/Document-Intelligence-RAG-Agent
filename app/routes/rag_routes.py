from fastapi import APIRouter, UploadFile, File
import shutil

from app.services.rag_pipeline import (
    create_vecor_db,
    query_vector_db
)

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    message = create_vecor_db(file_path)

    return {
        "message": message
    }

@router.get("/ask")
def ask(query: str):
    try:
        answer = query_vector_db(query)
        return {
            "answer": answer
        }
    except ValueError as e:
        return {
            "error": str(e)
        }