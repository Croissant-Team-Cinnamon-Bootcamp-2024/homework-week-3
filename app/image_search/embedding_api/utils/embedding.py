from functools import lru_cache
from typing import List

import clip
import torch

from .queryimage import QueryImage


@lru_cache
def load_clip_model(model_name, device="cpu"):
    # Load the CLIP model
    model, preprocess = clip.load(model_name, device=device)
    return model, preprocess


def get_image_embeddings(
    query_images: QueryImage, model_name="ViT-B/32", batch_size=32, device="cpu"
) -> List[List[float]]:
    model, preprocess = load_clip_model(model_name, device)

    # List to store image embeddings
    image_embeddings = []

    # Process images in batches
    with torch.no_grad():
        for i in range(0, len(query_images.images), batch_size):
            batch_images = query_images.images[i : i + batch_size]
            preprocessed_images = torch.stack(
                [preprocess(image) for image in batch_images]
            ).to(device)
            embeddings = model.encode_image(preprocessed_images)
            embeddings /= embeddings.norm(dim=-1, keepdim=True)
            image_embeddings.extend(embeddings.cpu().numpy().tolist())

    return image_embeddings
