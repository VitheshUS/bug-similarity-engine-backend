# Semantic Bug Search System

A semantic bug retrieval platform built using FastAPI, Angular, Sentence Transformers, and FAISS for context-aware issue matching.

Instead of relying on traditional keyword-based search, the system uses transformer-generated embeddings and vector similarity search to retrieve semantically related bugs and duplicate issues.

---

## Features

* Semantic bug search using vector embeddings
* FAISS-powered nearest neighbor retrieval
* Context-aware issue matching using cosine similarity
* Incremental FAISS index updates without full re-indexing
* FastAPI-based REST API backend
* Angular frontend for natural language search
* Dockerized local orchestration
* NGINX reverse proxy configuration
* Real-time semantic retrieval results

---

## Tech Stack

### Backend

* Python
* FastAPI
* Sentence Transformers
* FAISS
* NumPy

### Frontend

* Angular
* TypeScript
* HTML
* CSS

### Infrastructure

* Docker
* NGINX

---

## Architecture Overview

```text
User Query
    ↓
Angular Frontend
    ↓
FastAPI Backend
    ↓
Embedding Generation
(Sentence Transformers)
    ↓
FAISS Vector Search
    ↓
Ranked Semantic Results
```

---

## How Semantic Search Works

1. Bug descriptions are converted into dense vector embeddings using Sentence Transformers.
2. Embeddings are stored inside a FAISS vector index.
3. User queries are converted into embeddings in real time.
4. Cosine similarity search retrieves semantically related bugs.
5. Results are ranked based on similarity score.

Unlike keyword-based search, this approach can identify contextually similar issues even when exact words do not match.

---

## Project Structure

```text
semantic-bug-search/
│
├── backend/
│   ├── app/
│   ├── data/
│   ├── faiss_index/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── nginx/
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## API Endpoint

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
cd semantic-bug-search
```

---

## Backend Setup

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

### Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

## Frontend Setup

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

### Build Containers

```bash
docker-compose build
```

### Run Application

```bash
docker-compose up
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

* Hybrid semantic + keyword search
* Redis caching for faster retrieval
* Authentication and role-based access
* Streaming search suggestions
* Cloud deployment
* Search filtering and categorization
* AI-generated bug summaries

---

## Author

Vithesh U S
