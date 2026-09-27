from sqlmodel import SQLModel, Field
from typing import Optional


class Claim(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str
    severity: str
    action: str
    metadata_json: Optional[str]
