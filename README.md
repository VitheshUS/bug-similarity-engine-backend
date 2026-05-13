# Semantic Bug Search System — Backend

A semantic bug retrieval system built using FastAPI, Sentence Transformers, and FAISS for context-aware issue matching.

Instead of relying on traditional keyword-based search, the system uses transformer-generated embeddings and vector similarity search to retrieve semantically related bugs and duplicate issues.

---

## Features

- Semantic bug search using vector embeddings
- FAISS-powered nearest neighbor retrieval
- FastAPI-based REST API architecture
- Incremental FAISS index updates without full re-indexing
- JSON-based ingestion pipeline
- Cosine similarity–based contextual matching
- Dockerized backend setup

---

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- FAISS
- NumPy
- Docker
- NGINX

---

## Architecture Overview

```text
Bug Data (JSON)
       ↓
Embedding Generation (Sentence Transformers)
       ↓
Vector Storage (FAISS Index)
       ↓
FastAPI Search API
       ↓
Semantic Retrieval Results
How Semantic Search Works
Bug descriptions are converted into dense vector embeddings using Sentence Transformers.
Embeddings are stored inside a FAISS vector index.
User queries are converted into embeddings in real time.
Cosine similarity search retrieves semantically related bugs.
Results are ranked based on similarity score.

Unlike keyword search, this approach can identify contextually similar issues even when exact words do not match.

Project Structure
backend/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── embeddings/
│   └── utils/
│
├── data/
├── faiss_index/
├── requirements.txt
├── Dockerfile
└── main.py
API Endpoints
Search Bugs
POST /search

Request:

{
  "query": "login page crashes after token expiration"
}

Response:

{
  "results": [
    {
      "bug_id": 101,
      "similarity": 0.91,
      "description": "application crashes when JWT token expires"
    }
  ]
}
Local Setup
Clone Repository
git clone <repo-url>
cd backend
Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run Application
uvicorn main:app --reload

Application runs on:

http://localhost:8000
Docker Setup
Build Docker Image
docker build -t semantic-search-backend .
Run Container
docker run -p 8000:8000 semantic-search-backend
Future Improvements
Hybrid semantic + keyword search
Redis caching for faster retrieval
Authentication and role-based access
Streaming search suggestions
Cloud deployment
Support for larger embedding models
Author

Vithesh U S
