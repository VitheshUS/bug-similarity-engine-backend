from fastapi import FastAPI,Depends
from app.service.search_service import SearchService
from app.infrastructure.data_repository import DataRepository
from app.service.embedding_service import EmbeddingService
from app.infrastructure.index import index
from sentence_transformers import SentenceTransformer

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
    return SentenceTransformer('all-MiniLM-L6-v2')

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


#Controller-Endpoint
@app.get('/search-match')
def getSimilarMatch(
    query:str,
    search_service:SearchService=Depends(get_search_service)
    ):
    try:
        matches = search_service.getMatches(query)
        return {"status": "SUCCESS", "result": matches}
    except Exception as e:
        print("ERROR:", str(e))
        return {"status": "ERROR", "message": str(e)}