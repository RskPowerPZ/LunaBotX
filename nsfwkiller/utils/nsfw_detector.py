import cv2
import io
import tempfile
import os
from PIL import Image
from transformers import pipeline
from nudenet import NudeDetector   # ← Correct import (NudeNet nahi, NudeDetector hai)
from loguru import logger
from config import NSFW_THRESHOLD

nsfw_classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection", device="cpu")
nude_detector = NudeDetector()   # Global instance (first run pe model download ho jaayega)

async def is_nsfw(file_bytes: bytes, content_type: str = "photo"):
    try:
        # Falconsai NSFW model (fast & accurate for photos/GIF/stickers)
        if content_type in ["photo", "sticker", "animation"]:
            image = Image.open(io.BytesIO(file_bytes)).convert("RGB")
            results = nsfw_classifier(image)
            for r in results:
                if r['label'].lower() in ['porn', 'hentai', 'sexy', 'nudity'] and r['score'] > NSFW_THRESHOLD:
                    return True, r['score']

        # Video ke liye first frame + OpenCV
        elif content_type == "video":
            video = cv2.VideoCapture(io.BytesIO(file_bytes))
            success, frame = video.read()
            if success:
                pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                results = nsfw_classifier(pil_frame)
                for r in results:
                    if r['label'].lower() in ['porn', 'hentai', 'sexy', 'nudity'] and r['score'] > NSFW_THRESHOLD:
                        return True, r['score']
            video.release()

        # NudeDetector fallback (correct usage)
        # NudeDetector file path expect karta hai isliye temp file bana rahe hain
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name

        detections = nude_detector.detect(tmp_path)
        os.unlink(tmp_path)  # clean up

        # Agar koi nudity detection mila toh NSFW
        if detections and len(detections) > 0:
            return True, 0.95

        return False, 0.0

    except Exception as e:
        logger.error(f"NSFW detection error: {e}")
        return False, 0.0
