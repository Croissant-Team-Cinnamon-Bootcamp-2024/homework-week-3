import json
from typing import List

import requests
from fastapi import UploadFile


def load_image_path(save_path):
    with open(save_path, 'r') as file:
        data = json.load(file)
    return data


def get_embeddings(url, images: List[UploadFile]) -> List[List[float]]:
    files = []
    for image in images:
        contents = image.file.read()
        files.append(("files", contents))

    r = requests.post(url, files=files)

    if r.status_code != 200:
        raise Exception("Failed to send request to Embedding API")

    return r.json()["embeddings"]


def search(url, embedded_vector: List[List[float]]) -> List[List[int]]:
    r = requests.post(
        url,
        json={
            "embeddings": embedded_vector,
        },
    )
    if r.status_code != 200:
        raise Exception("Failed to send request to Search API")
    return r.json()


async def search_images(embedding_url, search_url, files):
    """
    Find similar images in database

    Args:
        files: List[UploadFile]
    Returns:
        List[List[int]]: List of lists of indexes of similar images
    """
    # byte_image = await file.read()
    embedded_vector = get_embeddings(embedding_url, files)
    results = search(search_url, embedded_vector)
    return results
