import pytest
from fastapi.testclient import TestClient
from main import app
import numpy as np

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Image Embedding API"}

def test_embed_image_success():
    # You'll need a valid image URL for this test
    valid_image_url = "https://cdn.tuoitre.vn/thumb_w/730/471584752817336320/2024/4/7/thu-y-read-only-1712454975600469786440.jpg"
    response = client.post("/embed-image/", json={"url": valid_image_url})
    assert response.status_code == 200
    data = response.json()
    assert "embeddings" in data
    assert isinstance(data["embeddings"], list)
    assert len(data["embeddings"]) > 0
    # Assuming you're using Option 2 (converting to lists)
    assert isinstance(data["embeddings"][0], list)

def test_embed_image_invalid_url():
    invalid_image_url = "https://example.com/nonexistent-image.jpg"
    response = client.post("/embed-image/", json={"url": invalid_image_url})
    assert response.status_code == 500

# @pytest.fixture
# def mock_get_image_embeddings(monkeypatch):
#     def mock_embeddings(*args, **kwargs):
#         return [np.random.rand(512).astype(np.float32).tolist()]
#     monkeypatch.setattr("main.get_image_embeddings", mock_embeddings)

# def test_embed_image_mocked(mock_get_image_embeddings):
#     valid_image_url = "https://cdn.tuoitre.vn/thumb_w/730/471584752817336320/2024/4/7/thu-y-read-only-1712454975600469786440.jpg"
#     response = client.post("/embed-image/", json={"url": valid_image_url})
#     assert response.status_code == 200
#     data = response.json()
#     assert "embeddings" in data
#     assert isinstance(data["embeddings"], list)
#     assert len(data["embeddings"]) == 1
#     assert len(data["embeddings"][0]) == 512