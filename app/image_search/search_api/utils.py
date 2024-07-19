import clip
import faiss
import glob
import json
from PIL import Image
from typing import List
import numpy as np

index_path = "/shared/data/hw3/index.faiss"

def load_faiss_index(index_path):
    # Load FAISS index
    index = faiss.read_index(index_path)
    
    return index

def faiss_get_similar_images(images: List[List[float]], top_k=5):
    
    images = np.array(images)
    
    # Get index and image_paths of all images
    index = load_faiss_index(index_path)
        
    # Search for similar images
    D, I = index.search(images, top_k)
    
    return I.tolist(), D
    

if __name__ == "__main__":
    query = np.random.rand(3, 512)
    
    # Get similar images
    similar_image_indices, D = faiss_get_similar_images(query, top_k=5)
    
    # Print the indices of similar images
    print("Indices of similar images:", similar_image_indices)
    # print(D)



