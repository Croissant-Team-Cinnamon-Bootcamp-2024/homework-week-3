from typing import List

import faiss
import numpy as np

index_path = "/shared/data/hw3/index.faiss"


class FaissHelper:
    def __init__(self, index_path):
        # Load FAISS index
        self.index = faiss.read_index(index_path)

    def get_similar_images(self, images: List[List[float]], top_k=5):
        images = np.array(images)

        # Search for similar images
        distances, indices = self.index.search(images, top_k)

        return indices.tolist(), distances


if __name__ == "__main__":
    query = np.random.rand(3, 512)

    faiss_helper = FaissHelper(index_path)
    # Get similar images
    similar_image_indices, D = faiss_helper.get_similar_images(query, top_k=5)

    # Print the indices of similar images
    print("Indices of similar images:", similar_image_indices)
    # print(D)
