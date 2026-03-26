from fastapi import FastAPI,Depends, Request
from fastapi.responses import JSONResponse
from sentence_transformers import SentenceTransformer
from app.application.search_service import SearchService
from app.infrastructure.data_repository import DataRepository
from app.infrastructure.embedding_service import EmbeddingService
from app.infrastructure.index import index
from app.domain.model.api.response import ApiResponse
from app.config import SUCCESS_STATUS,ERROR_STATUS
from app.domain.validator import ApiValidator
from app.infrastructure.embeddingModel import EmbeddingModel

#Singleton instances
embedding_model=SentenceTransformer('all-MiniLM-L6-v2')


#Initialize FastAPI app
app=FastAPI()

#Dependency Injection

#Repository
def get_repository():
    return DataRepository() 

#FAISS index
def get_index():
    return index

#Sentence transformer model
def get_embedding_model():
    return EmbeddingModel(embedding_model)

#Embedding service
def get_embedding_service(
    model=Depends(get_embedding_model),
    data_store=Depends(get_repository)
):
    return EmbeddingService(model,data_store)

#search service
def get_search_service(
        repository:DataRepository=Depends(get_repository),
        index=Depends(get_index),
        embedding_service:EmbeddingService=Depends(get_embedding_service)
    ):
    return SearchService(repository,index,embedding_service)

#Exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    print(f"Error: {exc}")
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