from typing import List

from pydantic import BaseModel


class QueryEmbeddings(BaseModel):
    embeddings: List[List[float]]
