from typing import List

from fastapi import UploadFile
from pydantic import BaseModel


class QueryFiles(BaseModel):
    images: List[UploadFile]


class EmbeddingResponse(BaseModel):
    embeddings: List[List[float]]
