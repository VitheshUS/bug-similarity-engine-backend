from app.repository import data_repository as dr
from app.service import embedding_service as es
from app.utils import similarity as similarity_check
from app.service import index_service as ids
import numpy as np

K=3
THRESHOLD=0.6

def getMatches(query:str):
    try:
        embeddings=dr.get_embeddings()

        queryEmbedding=es.generate_embedding(query).reshape(1,-1)

        similarities=similarity_check.compute_similarity(queryEmbedding,embeddings)

        similarities_filtered=similarities[similarities > THRESHOLD]

        similarities_sorted=similarities_filtered.argsort()

        similarities_top_matches=similarities_sorted[-K:]

        similarities_top_matches_desc=similarities_top_matches[::-1]

        similar_matches=[]

        queries=dr.get_queries()
        for index in similarities_top_matches_desc:
            similar_matches.append(
                {
                    "query":queries[index],
                    "score":round(float(similarities[index]),2)
                }
            )

        test_FAISS(embeddings,queryEmbedding)

        return similar_matches
    except Exception as e:
        raise

def test_FAISS(embeddings,query_embeddings):
    print("performing faiss check")
    
    index=ids.build_index(embeddings)

    print(index)

    similarity_score,indices=ids.search_index(index,query_embeddings,2)

    print(similarity_score,indices)
