from fastapi import FastAPI,Depends, Request
from fastapi.responses import JSONResponse
from sentence_transformers import SentenceTransformer
from app.application.search_service import SearchService
from app.application.insert_service import InsertService
from app.infrastructure.data_repository import DataRepository
from app.infrastructure.embedding_service import EmbeddingService
from app.domain.model.api.response import ApiResponse
from app.config import SUCCESS_STATUS,ERROR_STATUS
from app.domain.validator import ApiValidator
from app.infrastructure.embeddingModel import EmbeddingModel
from app.infrastructure.index import FaissIndex
from contextlib import asynccontextmanager
import logging
import time
from fastapi.middleware.cors import CORSMiddleware
from app.domain.model.api.addQuery import AddQuery
from app.domain.loader import Loader

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

    app.state.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    repository = get_repository()
    embedding_service = EmbeddingService(EmbeddingModel(app.state.embedding_model), repository)
    loader = Loader(embedding_service)
    loader.clear_data()  # Clear existing data and embeddings before loading new data
    loader.load_data()

    embeddings = repository.get_embeddings()
    app.state.index = get_faiss_index(embeddings)

    yield

    #Any shutdown code can be placed here
    logger.info("Application is shutting down...")


#Initialize FastAPI app
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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

def get_loader(embedding_service:EmbeddingService=Depends(get_embedding_service)):
    return Loader(embedding_service)

#search service
def get_search_service(
        repository:DataRepository=Depends(get_repository),
        index=Depends(get_index),
        embedding_service:EmbeddingService=Depends(get_embedding_service),
        logger:logging.Logger=Depends(get_logger)
    ):
    return SearchService(repository,index,embedding_service,logger)

#insert service
def get_insert_service(
        repository:DataRepository=Depends(get_repository),
        index=Depends(get_index),
        embedding_service:EmbeddingService=Depends(get_embedding_service),
        logger:logging.Logger=Depends(get_logger)
    ):
    return InsertService(repository,index,embedding_service,logger)

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

        start_time=time.time() #logging the start time of the request handling

        matches = search_service.getMatches(query)

        end_time=time.time() #logging the end time of the request handling

        logger.info({
            "event": "Search operation",
            "query": query,
            "matches_found": len(matches),
            "latency": f"{round(end_time-start_time,2)} seconds"
        })

        return JSONResponse(
            status_code=200,
            content={
                "status": SUCCESS_STATUS,
                "result": matches
            }
        )

@app.post('/add-query')
def add_query(
    request:AddQuery,
    insert_service:InsertService=Depends(get_insert_service)
):
    #Validate the query parameter
    ApiValidator.validate_query(request.query)

    insert_service.addQuery(request.query)

    return JSONResponse(
        status_code=200,
        content={
            "status": SUCCESS_STATUS,
            "message": "Query added successfully"
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