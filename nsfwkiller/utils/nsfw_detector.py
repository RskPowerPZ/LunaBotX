import cv2
import io
from PIL import Image
from transformers import pipeline
from nudenet import NudeNet
from loguru import logger
from config import NSFW_THRESHOLD

nsfw_classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection", device="cpu")
nudenet = NudeNet()

async def is_nsfw(file_bytes: bytes, content_type: str = "photo"):
    try:
        if content_type in ["photo", "sticker", "animation"]:
            image = Image.open(io.BytesIO(file_bytes)).convert("RGB")
            results = nsfw_classifier(image)
            for r in results:
                if r['label'].lower() in ['porn', 'hentai', 'sexy', 'nudity'] and r['score'] > NSFW_THRESHOLD:
                    return True, r['score']
        elif content_type == "video":
            video = cv2.VideoCapture(io.BytesIO(file_bytes))
            success, frame = video.read()
            if success:
                pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                results = nsfw_classifier(pil_frame)
                for r in results:
                    if r['label'].lower() in ['porn', 'hentai', 'sexy', 'nudity'] and r['score'] > NSFW_THRESHOLD:
                        return True, r['score']
                if nudenet.detect(pil_frame):
                    return True, 0.95
            video.release()
        if nudenet.detect(Image.open(io.BytesIO(file_bytes))):
            return True, 0.95
        return False, 0.0
    except Exception as e:
        logger.error(f"NSFW detection error: {e}")
        return False, 0.0
