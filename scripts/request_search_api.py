import numpy as np
import requests

query = np.random.rand(3, 512)

r = requests.post(
    'http://localhost:8000/search',
    json={
        "embeddings": query.tolist(),
    },
)

print(r.json())
