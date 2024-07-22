# Image-to-Image Search Service

## Overview

This project is part of the CinnamonAI Bootcamp (Week 3, Day 2) assignment. It implements an image-to-image search service using the COCO 128 dataset. The system uses CLIP for image encoding and FAISS for the search algorithm.

## System Design

![System Design Diagram](path/to/system_design_diagram.png)

The project consists of three main API services:

1. **Embedding API**: Extracts image embeddings using the CLIP model.
2. **Search API**: Performs similarity search using FAISS.
3. **Aggregate API**: Orchestrates the process and handles user requests.

### Workflow

1. User sends image(s) to the Aggregate API.
2. Aggregate API forwards the image(s) to the Embedding API.
3. Embedding API returns embedding vector(s).
4. Aggregate API sends the vector(s) to the Search API.
5. Search API returns the indexes of the top 5 most similar images for each vector.
6. Aggregate API retrieves the corresponding images from storage and returns them to the user.

## Features

- Multi-image input support
- Top-5 similar images returned for each input image
- Containerized microservices architecture
- Deployed on AWS

## Technologies Used

- Python
- FastAPI
- Docker
- CLIP (for image encoding)
- FAISS (for similarity search)
- AWS (for deployment)
- CI/CD
- Pre-commit hooks

## API Endpoints

### 1. Embedding API

- **Input**: List of images (BytesIO format)
- **Output**: List of embedding vectors (numpy arrays)
- **Endpoint**: `/embed`

### 2. Search API

- **Input**: List of embedding vectors
- **Output**: List of lists containing top 5 image indexes
- **Endpoint**: `/search`

### 3. Aggregate API

- **Input**: One or more images
- **Output**: Top 5 most similar images for each input image
- **Endpoint**: `/search_images`

## Setup and Installation

(Include instructions for setting up the project locally, including Docker commands)

## Deployment

The APIs are deployed on AWS. The final endpoint for the Aggregate API is: `https://your-aws-endpoint.com/search_images`

## Development

We follow a branching strategy for development:

- `feat/embedding-core`: Core logic for Embedding API
- `feat/embedding-api`: FastAPI and Docker setup for Embedding API
- `feat/search-core`: Core logic for Search API
- `feat/search-api`: FastAPI and Docker setup for Search API
- `feat/aggregate-api`: Complete implementation of Aggregate API

Merged branches:
- `merge/embedding-api`
- `merge/search-api`

## Code Quality

We maintain high code quality standards through:
- Continuous Integration (CI)
- Code conventions
- Unit testing
- Docstrings
- Pre-commit hooks

## Contributors

- Hưng
- Hoàng
- Thảo
- Huy
- Tùng

## License

(Include your license information here)
