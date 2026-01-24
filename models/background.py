from transformers import pipeline
from PIL import Image
import numpy as np

segmenter = pipeline(
    "mask-generation",
    model="facebook/sam-vit-base"
)

def make_white_background(image_path):
    image = Image.open(image_path).convert("RGB")
    masks = segmenter(image)

    mask = masks[0]["mask"]
    image_np = np.array(image)
    white_bg = np.ones_like(image_np) * 255

    final = np.where(mask[..., None], image_np, white_bg)
    output = Image.fromarray(final.astype("uint8"))
    output.save("output_white_bg.png")

    return "output_white_bg.png"
