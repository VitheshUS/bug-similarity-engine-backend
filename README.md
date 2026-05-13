# Semantic Bug Search System — README Templates

---

# Backend README

````md
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
````

---

## How Semantic Search Works

1. Bug descriptions are converted into dense vector embeddings using Sentence Transformers.
2. Embeddings are stored inside a FAISS vector index.
3. User queries are converted into embeddings in real time.
4. Cosine similarity search retrieves semantically related bugs.
5. Results are ranked based on similarity score.

Unlike keyword search, this approach can identify contextually similar issues even when exact words do not match.

---

## Project Structure

```text
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
```

---

## API Endpoints

### Search Bugs

```http
POST /search
```

Request:

```json
{
  "query": "login page crashes after token expiration"
}
```

Response:

```json
{
  "results": [
    {
      "bug_id": 101,
      "similarity": 0.91,
      "description": "application crashes when JWT token expires"
    }
  ]
}
```

---

## Local Setup

### Clone Repository

```bash
git clone <repo-url>
cd backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn main:app --reload
```

Application runs on:

```text
http://localhost:8000
```

---

## Docker Setup

### Build Docker Image

```bash
docker build -t semantic-search-backend .
```

### Run Container

```bash
docker run -p 8000:8000 semantic-search-backend
```

---

## Future Improvements

* Hybrid semantic + keyword search
* Redis caching for faster retrieval
* Authentication and role-based access
* Streaming search suggestions
* Cloud deployment
* Support for larger embedding models

---

## Author

Vithesh U S

````

---

# Frontend README

```md
# Semantic Bug Search System — Frontend

Frontend application for a semantic bug retrieval platform built using Angular.

The UI allows users to search for semantically related bugs using natural language queries and view ranked similarity results retrieved from the FastAPI backend.

---

## Features

- Natural language bug search
- Real-time semantic retrieval results
- Similarity score visualization
- Responsive Angular UI
- REST API integration with FastAPI backend
- Dockerized frontend setup
- NGINX-based serving and reverse proxy configuration

---

## Tech Stack

- Angular
- TypeScript
- HTML
- CSS
- Docker
- NGINX

---

## Application Flow

```text
User Query
    ↓
Angular Frontend
    ↓
FastAPI Backend
    ↓
Embedding + FAISS Search
    ↓
Ranked Semantic Results
````

---

## Project Structure

```text
frontend/
│
├── src/
│   ├── app/
│   ├── assets/
│   ├── environments/
│   └── styles/
│
├── nginx/
├── Dockerfile
├── angular.json
└── package.json
```

---

## Screenshots

Add screenshots or GIFs here.

Example:

* Search interface
* Semantic result ranking
* Similarity score display

---

## Local Setup

### Install Dependencies

```bash
npm install
```

### Run Angular Application

```bash
ng serve
```

Frontend runs on:

```text
http://localhost:4200
```

---

## Docker Setup

### Build Docker Image

```bash
docker build -t semantic-search-frontend .
```

### Run Container

```bash
docker run -p 4200:80 semantic-search-frontend
```

---

## NGINX Configuration

NGINX is used for:

* Serving Angular static files
* Reverse proxying API requests
* Simplifying local container orchestration

Example:

```nginx
location /api/ {
    proxy_pass http://backend:8000/;
}
```

---

## Future Improvements

* Search filters and categorization
* Authentication and user roles
* Search history
* Dark mode
* Infinite scrolling for results
