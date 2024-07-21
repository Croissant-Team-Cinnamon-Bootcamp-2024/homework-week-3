import os
import uuid
from typing import List

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from utils import load_image_path, search_images

load_dotenv()
SEARCH_URL = f'{os.getenv("SEARCH_API_URL")}/search'
data = load_image_path(os.getenv("IMAGES_PATH_FILE"))
app = FastAPI()

# Create a directory to store uploaded files
upload_dir = os.getenv("UPLOAD_DIR")
os.makedirs(upload_dir, exist_ok=True)
app.mount("/data", StaticFiles(directory="data"), name="data")


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    search_results = await search_images(SEARCH_URL, files)
    saved_file_urls = []

    for file in files:
        file_extension = file.filename.split(".")[-1]
        file_id = str(uuid.uuid4())
        file_path = os.path.join(upload_dir, f"{file_id}.{file_extension}")

        with open(file_path, "wb") as f:
            await file.seek(0)
            f.write(await file.read())

        saved_file_urls.append(
            os.path.join("/" + upload_dir, f"{file_id}.{file_extension}")
        )

    response_content = "<html><body>"
    for i, file_url in enumerate(saved_file_urls):
        response_content += '<h3>Uploaded Image:</h3>'
        response_content += f'<img src="{file_url}" alt="Uploaded Image" style="width:200px;height:auto;">'
        response_content += '<h3>Similar Images:</h3>'
        for index in search_results[i]:
            similar_image_url = "/" + data[index]
            response_content += f'<img src="{similar_image_url}" alt="Similar Image" style="width:200px;height:auto;">'
        response_content += "<hr>"
    response_content += "</body></html>"

    return HTMLResponse(content=response_content)


@app.get("/")
async def home():
    content = """
    <body>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
    </body>
    """
    return HTMLResponse(content=content)


def main():
    # Run web server with uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv("AGG_FASTAPI_HOST", "127.0.0.1"),
        port=int(os.getenv("AGG_FASTAPI_PORT", 8000)),
        # reload=True,  # Uncomment this for debug
        workers=2,
    )


if __name__ == "__main__":
    main()
