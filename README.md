# Insurance-claim-triage-agent-
Multimodal insurance claim triage agent

Overview
--------
This project provides a production-ready skeleton for a multimodal insurance claim triage agent. It accepts image uploads, runs a triage pipeline (vision adapter + heuristic), persists results, and exposes a REST API.

Quickstart (local)
-------------------
1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\Activate.ps1 # Windows PowerShell
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

4. Open interactive docs at `http://localhost:8080/docs` and POST an image to `/api/triage`.

Docker
------
Build and run with Docker:

```bash
docker build -t claim-triage .
docker run -p 8080:8080 claim-triage
# or with docker-compose
docker compose up --build
```

Testing
-------
Run the test suite with:

```bash
pytest -q
```

Project layout
--------------
- `app/` - FastAPI application
- `app/services/triage.py` - triage pipeline
- `app/adapters/vision_adapter.py` - vision adapter (placeholder)
- `app/models/db.py` - SQLModel database models
- `app/db.py` - DB session helpers
- `Dockerfile`, `docker-compose.yml` - container setup
- `tests/` - automated tests

Next steps
----------
- Replace `vision_adapter` with a real detector (YOLO, segmenter, or cloud API).
- Add authentication, rate limiting, and request validation.
- Add retries and observability (logging, metrics, tracing).

