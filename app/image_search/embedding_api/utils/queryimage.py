from dataclasses import dataclass
from typing import List
from PIL import Image

@dataclass
class QueryImage:
    images: List[Image.Image]
