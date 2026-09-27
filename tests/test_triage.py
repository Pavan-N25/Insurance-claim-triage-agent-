from fastapi.testclient import TestClient
from app.main import app
import io
from PIL import Image


def create_test_image(color=(255, 0, 0), size=(100, 100)):
    img = Image.new("RGB", size, color)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


def test_triage_low():
    client = TestClient(app)
    img = create_test_image(size=(50, 50))
    files = {"file": ("img.png", img, "image/png")}
    resp = client.post("/api/triage", files=files)
    assert resp.status_code == 200
    data = resp.json()
    assert data["severity"] in ("low", "medium", "high")
