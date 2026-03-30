from fastapi import FastAPI,Depends, Request
from fastapi.responses import JSONResponse
from sentence_transformers import SentenceTransformer
from app.application.search_service import SearchService
from app.infrastructure.data_repository import DataRepository
from app.infrastructure.embedding_service import EmbeddingService
from app.domain.model.api.response import ApiResponse
from app.config import SUCCESS_STATUS,ERROR_STATUS
from app.domain.validator import ApiValidator
from app.infrastructure.embeddingModel import EmbeddingModel
from app.infrastructure.index import FaissIndex
from contextlib import asynccontextmanager
import logging

logging.basicConfig(
    level=logging.INFO,  # show INFO and above
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

#startup event
@asynccontextmanager
async def lifespan(app: FastAPI):
    #Any startup code can be placed here
    logger.info("Application is starting up...")

    repository=get_repository()
    embeddings=repository.get_embeddings()
    app.state.embedding_model=SentenceTransformer('all-MiniLM-L6-v2')
    app.state.index=get_faiss_index(embeddings)

    yield

    #Any shutdown code can be placed here
    logger.info("Application is shutting down...")


#Initialize FastAPI app
app = FastAPI(lifespan=lifespan)

#Dependency Injection

#Repository
def get_repository():
    return DataRepository() 

#Sentence transformer model
def get_embedding_model(request: Request):
    return EmbeddingModel(request.app.state.embedding_model)

#Get Faiss index
def get_faiss_index(embeddings):
    return FaissIndex(embeddings)   

#Embedding service
def get_embedding_service(
    model=Depends(get_embedding_model),
    data_store=Depends(get_repository)
):
    return EmbeddingService(model,data_store)

def get_index(request: Request):
    return request.app.state.index

def get_logger():
    return logger

#search service
def get_search_service(
        repository:DataRepository=Depends(get_repository),
        index=Depends(get_index),
        embedding_service:EmbeddingService=Depends(get_embedding_service),
        logger:logging.Logger=Depends(get_logger)
    ):
    return SearchService(repository,index,embedding_service,logger)

#Exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    logger.error(f"Error: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "status": ERROR_STATUS,
            "message": "Internal server error"
        }
    )

#Controller-Endpoint
@app.get('/search-match')
def getSimilarMatch(
    query:str,
    search_service:SearchService=Depends(get_search_service)
    ):
        #Validate the query parameter
        ApiValidator.validate_query(query)

        matches = search_service.getMatches(query)

        return JSONResponse(
            status_code=200,
            content={
                "status": SUCCESS_STATUS,
                "result": matches
            }
        )

@app.get('/health')
def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": SUCCESS_STATUS,
            "message": "API is healthy"
        }
    )

@app.get('/ready')
def readiness_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": SUCCESS_STATUS,
            "message": "API is ready"
        }
    )