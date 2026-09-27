from PIL import Image
import io


def detect_damage(image_bytes: bytes) -> dict:
    # placeholder damage detection: check if mostly dark
    img = Image.open(io.BytesIO(image_bytes)).convert("L")
    pixels = list(img.getdata())
    avg = sum(pixels) / len(pixels)
    damage_likelihood = max(0.0, min(1.0, (128 - avg) / 128))
    return {"damage_score": damage_likelihood}
