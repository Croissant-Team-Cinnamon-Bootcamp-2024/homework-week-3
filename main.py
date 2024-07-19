import argparse
import io
from fastapi import FastAPI, UploadFile
from PIL import Image
import numpy as np

@app.post("/search")
async def search_image(file: UploadFile):
    """
    Find similar images in database
    
    Args:
        file: UploadFile
    Returns:
        List[]: List of indexs of similar image
    
    """
    byte_image = await file.read()
    image = Image.open(io.BytesIO(byte_image))
    embedded_vector: np.ndarray = get_to_Embedding_vector(byte_image)

    results:np.ndarray = search(embedded_vector)

    






if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", type=int, default=8000)
    # parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    # print(f"Listening on port {args.port}")
    # uvicorn.run("main:app", host="0.0.0.0", port=args.port, reload=True)