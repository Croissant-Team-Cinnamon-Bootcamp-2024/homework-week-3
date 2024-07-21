import io
import os
from typing import List

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile
from PIL import Image
from pydantic import BaseModel
from utils.embedding import get_image_embeddings
from utils.queryimage import QueryImage

load_dotenv()
app = FastAPI(title="embedding API")


class EmbeddingResponse(BaseModel):
    embeddings: List[List[float]]


@app.post("/embed-image/", response_model=EmbeddingResponse)
async def embed_image(files: List[UploadFile]):
    try:
        images = []
        for file in files:
            image_content = await file.read()
            images.append(Image.open(io.BytesIO(image_content)))

        # Create a QueryImage object
        query_images = QueryImage(images)
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
        host=os.getenv("EMBEDDING_FASTAPI_HOST", "127.0.0.1"),
        port=int(os.getenv("EMBEDDING_FASTAPI_PORT", 8002)),
        # reload=True,  # Uncomment this for debug
        workers=2,
    )


if __name__ == "__main__":
    main()
