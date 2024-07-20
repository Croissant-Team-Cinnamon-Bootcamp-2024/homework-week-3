import torch
from PIL import Image
import numpy as np
import pytest
from app.image_search.embedding_api.utils.queryimage import QueryImage
from app.image_search.embedding_api.utils.embedding import get_image_embeddings

# Mocking the clip module and necessary methods
class MockModel:
    def encode_image(self, images):
        # Return a mock embedding: an array of the correct shape with random values
        return torch.randn((images.shape[0], 512))
    
    def eval(self):
        pass

def mock_clip_load(model_name, device):
    # Return a mock model and a mock preprocess function
    def mock_preprocess(image):
        # Simulate preprocessing by resizing to (3, 224, 224) and converting to tensor
        image = image.resize((224, 224))  # Ensure all images are resized to 224x224
        return torch.randn((3, 224, 224))
    
    return MockModel(), mock_preprocess

# Mock the clip module's load function
clip = type('clip', (), {'load': mock_clip_load})

@pytest.fixture(autouse=True)
def mock_clip(monkeypatch):
    monkeypatch.setattr('app.image_search.embedding_api.utils.embedding.clip', clip)

def test_get_image_embeddings():
    # Creating mock images of different sizes
    image1 = Image.new('RGB', (100, 150), color='red')  # Different size
    image2 = Image.new('RGB', (300, 300), color='blue') # Different size
    images = [image1, image2]  # Create a list of mock images

    # Create QueryImage object
    query_images = QueryImage(images=images)

    # Get embeddings
    embeddings = get_image_embeddings(query_images)

    # Assert embeddings is a list
    assert isinstance(embeddings, list)
    
    # Assert the correct number of batches (in this case, 1 batch since batch_size=32 > number of images)
    assert len(embeddings) == 1
    
    # Check that each numpy array in the list has the correct shape
    batch_embeddings = embeddings[0]  # Get the first batch
    assert isinstance(batch_embeddings, np.ndarray)
    assert batch_embeddings.shape == (len(images), 512)

if __name__ == "__main__":
    pytest.main()
