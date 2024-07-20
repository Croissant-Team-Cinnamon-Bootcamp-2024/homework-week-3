import clip
import torch
import numpy as np
from typing import List
from .queryimage import QueryImage

def get_image_embeddings(query_images: QueryImage, model_name="ViT-B/32", batch_size=32, device="cpu") -> List[np.ndarray]:
    # Load the CLIP model
    model, preprocess = clip.load(model_name, device=device)
    
    # List to store image embeddings
    image_embeddings = []

    # Process images in batches
    with torch.no_grad():
        for i in range(0, len(query_images.images), batch_size):
            batch_images = query_images.images[i:i+batch_size]
            preprocessed_images = torch.stack([preprocess(image) for image in batch_images]).to(device)
            embeddings = model.encode_image(preprocessed_images)
            embeddings /= embeddings.norm(dim=-1, keepdim=True)
            image_embeddings.append(embeddings.cpu().numpy())
    
    return image_embeddings
