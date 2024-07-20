import json

import numpy as np


def load_image_path(save_path):
    with open(save_path, 'r') as file:
        data = json.load(file)
    return data


def get_to_Embedding_vector(byte_image: bytes) -> np.ndarray:
    # Dummy implementation
    return np.random.rand(
        128
    )  # Example vector size, replace with your actual implementation


def search(embedded_vector: np.ndarray) -> np.ndarray:
    # Dummy implementation
    return np.random.randint(
        0, 100, 5
    )  # Example results, replace with your actual implementation


async def search_images(files):
    """
    Find similar images in database

    Args:
        files: List[UploadFile]
    Returns:
        List[List[int]]: List of lists of indexes of similar images
    """
    results = []
    for file in files:
        byte_image = await file.read()
        embedded_vector: np.ndarray = get_to_Embedding_vector(byte_image)
        result: np.ndarray = search(embedded_vector)
        results.append(result.tolist())
    return results
