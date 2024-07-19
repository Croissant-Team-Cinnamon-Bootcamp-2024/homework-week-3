import clip
import faiss
import glob
import json
from PIL import Image
from typing import List
import numpy as np

index_path = "data/index.faiss"
image_paths_path = "data/image_paths.json"
model_name = "ViT-B/32"

def load_faiss_index(index_path):
    # Load FAISS index
    index = faiss.read_index(index_path)
    
    return index

def faiss_get_similar_images(images: List[np.ndarray], top_k=5):
    
    # Get index and image_paths of all images
    index = load_faiss_index(index_path)
        
    # Search for similar images
    D, I = index.search(images, top_k)
    
    return I.tolist()
    

if __name__ == "__main__":
    query = np.random.rand(1, 512)
    # query_images = [
    #     "data/coco-128/test/000000000009_jpg.rf.6acc173402df5523069e146edb03ff4b.jpg",
    #     "data/coco-128/test/000000000283_jpg.rf.27927692baf616a7456bb3e24c21bfd7.jpg"
    # ]
    
    # # Load query images
    # images = [Image.open(image_path) for image_path in query_images]
    
    # Get similar images
    similar_image_indices = faiss_get_similar_images(query, top_k=5)
    
    # Print the indices of similar images
    print("Indices of similar images:", similar_image_indices)



