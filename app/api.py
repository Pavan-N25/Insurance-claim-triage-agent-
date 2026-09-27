from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from .services.triage import triage_claim
from .db import get_session
from .models.db import Claim
import json

router = APIRouter(prefix="/api")


class TriageResult(BaseModel):
    severity: str
    recommended_action: str
    details: dict


@router.post("/triage", response_model=TriageResult)
async def triage(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image uploads supported")
    content = await file.read()
    result = triage_claim(content)

    # persist
    session = get_session()
    claim = Claim(filename=file.filename, severity=result["severity"], action=result["recommended_action"], metadata_json=json.dumps(result["details"]))
    session.add(claim)
    session.commit()
    session.refresh(claim)
    session.close()

    return result
