from typing import Dict
from PIL import Image
import io
from ..adapters.vision_adapter import detect_damage


def analyze_image(img: Image.Image) -> Dict:
    # placeholder: basic size and mode
    return {"width": img.width, "height": img.height, "mode": img.mode}


def triage_claim(image_bytes: bytes) -> Dict:
    img = Image.open(io.BytesIO(image_bytes))
    analysis = analyze_image(img)

    # vision adapter damage score
    vision = detect_damage(image_bytes)

    # Simple heuristic using damage score and image area
    area = analysis["width"] * analysis["height"]
    score = vision.get("damage_score", 0)
    if score > 0.6 or area > 2_000_000:
        severity = "high"
        action = "urgent_inspection"
    elif score > 0.3 or area > 500_000:
        severity = "medium"
        action = "schedule_adjuster"
    else:
        severity = "low"
        action = "self_service"

    details = {**analysis, **vision}

    return {
        "severity": severity,
        "recommended_action": action,
        "details": details,
    }
