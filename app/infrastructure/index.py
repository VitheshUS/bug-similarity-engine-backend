import faiss
from app.infrastructure.data_repository import DataRepository


def get_index(embeddings):
    #Get the dimension of the numpy vector, here shape returns a tuple like (no. of vectors, length of vector(dimension))
    dimension=embeddings.shape[1]

    #Normalizing the magnitude to unit length, such that now only the directions are different
    #We basically removed the magnitude dependency
    faiss.normalize_L2(embeddings)

    #Now we need a index structure that internally configuers the search objects and saves the dimesion
    index=faiss.IndexFlatL2(dimension)

    #Now we will be storing the embeddings inside in this structure and later used for efficient similarity search
    index.add(embeddings)

    return index

def create_index():
    dr=DataRepository()
    embeddings=dr.get_embeddings()

    index=get_index(embeddings)

    return index

#Singleton instance of the index that can be used across the application
index=create_index()


def search_index(index,query_embedding,topK):
    #Important, Lower distance=More similar
    #Normalize the query embedding as well
    faiss.normalize_L2(query_embedding)

    #Get the similarity score and the indeces of each of these vectors
    similarity_scores,indices=index.search(query_embedding,topK)

    return similarity_scores[0],indices[0]