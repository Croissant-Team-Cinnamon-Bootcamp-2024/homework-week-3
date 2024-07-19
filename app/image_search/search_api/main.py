import os
from typing import List

# import torch
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

load_dotenv()
app = FastAPI(title="faiss search api")


def faiss_search_dummy(embeddings: List[List[float]]) -> List[List[int]]:
    """[A normal python function]
    Receive embedding of images and search for top-k similar images in the DB

    Args:
        embeddings (List[List[float]]): Embedding of images.

    Returns:
        List: List of top-k similar image IDs.
    """

    import numpy as np

    top_k = 5
    random_ids = np.random.randint(low=0, high=128, size=(len(embeddings), top_k))
    random_ids = random_ids.tolist()
    return random_ids


@app.get("/")
def home(request: Request):
    return JSONResponse({"message": "Hello, this is search API"})


class QueryEmbeddings(BaseModel):
    embeddings: List[List[float]]


@app.post("/search/")
async def predict(query_embeddings: QueryEmbeddings):
    """[FastAPI endpoint]
    Retrieve top-k similar images in the DB using query embeddings.

    Args:
        query_embeddings (QueryEmbeddings): Extracted image embeddings to query.

    Returns:
        dict: Dictionary of 1000 classes in ImageNet and their confidence scores (float).
    """
    input_data = query_embeddings.model_dump()
    search_result = faiss_search_dummy(embeddings=input_data["embeddings"])
    return search_result


def main():
    # Run web server with uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv("FASTAPI_HOST", "127.0.0.1"),
        port=int(os.getenv("FASTAPI_PORT", 8000)),
        # reload=True,  # Uncomment this for debug
    )


if __name__ == "__main__":
    main()
