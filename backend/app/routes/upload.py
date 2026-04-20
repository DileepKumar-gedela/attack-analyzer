from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.extractor import extract_text
from app.services.analyzer import advanced_analyze

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # ---- Read uploaded file ----
        contents: bytes = await file.read()

        if not contents:
            raise ValueError("Uploaded file is empty")

        # ---- Extract text ----
        text: str = extract_text(file.filename, contents)

        if not text.strip():
            raise ValueError("No readable text extracted from file")

        # ---- Advanced AI-style Analysis ----
        analysis = advanced_analyze(text)

        # ---- Final Response Payload ----
        response = {
            "filename": file.filename,
            "chars_extracted": len(text),
            "preview": text[:300],
            "analysis": analysis
        }

        return response

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Processing failed: {str(e)}"
        )
