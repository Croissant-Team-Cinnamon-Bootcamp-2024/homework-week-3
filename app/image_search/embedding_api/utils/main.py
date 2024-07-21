import os
import io
from typing import List

import requests
import uvicorn
import numpy as np
from dotenv import load_dotenv
from fastapi import FastAPI, Request,HTTPException
from pydantic import BaseModel
from PIL import Image


from embedding import get_image_embeddings
from queryimage import QueryImage



app = FastAPI(title="embedding API")


class ImageURL(BaseModel):
    url: str

class EmbeddingResponse(BaseModel):
    embeddings: List[np.ndarray]
    class Config:
        arbitrary_types_allowed = True

@app.post("/embed-image/", response_model=EmbeddingResponse)
async def embed_image(image_url: ImageURL):
    try:
        # Fetch the image from the provided URL
        response = requests.get(image_url.url)
        image = Image.open(io.BytesIO(response.content))
        
        # Create a QueryImage object
        query_images = QueryImage([image])
        
        # Get the embedding
        embeddings = get_image_embeddings(query_images)
        
        return EmbeddingResponse(embeddings=embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Image Embedding API"}


def main():
    # Run web server with uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv("SEARCH_FASTAPI_HOST", "127.0.0.1"),
        port=int(os.getenv("SEARCH_FASTAPI_PORT", 8002)),
        # reload=True,  # Uncomment this for debug
        workers=2,
    )


if __name__ == "__main__":
    main()