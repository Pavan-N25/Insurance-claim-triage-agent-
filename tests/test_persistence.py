from fastapi.testclient import TestClient
from app.main import app
from app.db import engine, create_db_and_tables
from app.models.db import Claim
from sqlmodel import Session, select
import io
from PIL import Image


def create_test_image(size=(100, 100)):
    img = Image.new("RGB", size, (0, 128, 255))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


def test_persistence(tmp_path):
    # ensure fresh DB
    create_db_and_tables()
    client = TestClient(app)
    img = create_test_image(size=(60, 60))
    files = {"file": ("img.png", img, "image/png")}
    resp = client.post("/api/triage", files=files)
    assert resp.status_code == 200

    with Session(engine) as session:
        stmt = select(Claim)
        results = session.exec(stmt).all()
        assert len(results) >= 1
