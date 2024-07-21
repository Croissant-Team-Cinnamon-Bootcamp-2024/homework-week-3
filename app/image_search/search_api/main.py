import os

# import torch
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from schemas import QueryEmbeddings
from utils import FaissHelper

load_dotenv()
app = FastAPI(title="faiss search api")
faiss_helper = FaissHelper(index_path=os.getenv("INDEX_SAVE_PATH"))


@app.get("/")
def home(request: Request):
    return JSONResponse({"message": "Hello, this is search API"})


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
    search_result, _ = faiss_helper.get_similar_images(
        embeddings=input_data["embeddings"]
    )
    return search_result


def main():
    # Run web server with uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv("SEARCH_FASTAPI_HOST", "127.0.0.1"),
        port=int(os.getenv("SEARCH_FASTAPI_PORT", 8001)),
        # reload=True,  # Uncomment this for debug
        workers=2,
    )


if __name__ == "__main__":
    main()
