import json
import os

import numpy as np
import requests
from dotenv import load_dotenv

load_dotenv()


def load_image_path(save_path):
    with open(save_path, 'r') as file:
        data = json.load(file)
    return data


def get_embeddings(byte_image: bytes) -> np.ndarray:
    # Dummy implementation
    return np.random.rand(
        len(byte_image), 512
    )  # Example vector size, replace with your actual implementation


# def search(embedded_vector: np.ndarray) -> np.ndarray:
#     # Dummy implementation
#     return np.random.randint(
#         0, 100, (len(embedded_vector), 5)
#     )  # Example results, replace with your actual implementation


def search(embedded_vector: np.ndarray) -> np.ndarray:
    r = requests.post(
        f'{os.getenv("SEARCH_API_HOST")}:{os.getenv("SEARCH_API_PORT")}/search',
        json={
            "embeddings": embedded_vector.tolist(),
        },
    )
    return r.json()


async def search_images(files):
    """
    Find similar images in database

    Args:
        files: List[UploadFile]
    Returns:
        List[List[int]]: List of lists of indexes of similar images
    """
    # byte_image = await file.read()
    embedded_vector = get_embeddings(files)
    results = search(embedded_vector)
    return results
