from app.utils import similarity as similarity_check
from app.infrastructure import index as ids
import numpy as np

class SearchService:
    K=3
    THRESHOLD=0.6

    def __init__(self,repository,index,embedding_service):
        self.repository=repository
        self.index=index
        self.embedding_service=embedding_service

    def getMatches(self,query:str):
        try:
            embeddings=self.repository.get_embeddings()

            queryEmbedding=self.embedding_service.generate_embedding(query).reshape(1,-1)

            similarities=similarity_check.compute_similarity(queryEmbedding,embeddings)

            similarities_filtered=similarities[similarities > SearchService.THRESHOLD]

            similarities_sorted=similarities_filtered.argsort()

            similarities_top_matches=similarities_sorted[-SearchService.K:]

            similarities_top_matches_desc=similarities_top_matches[::-1]

            similar_matches=[]

            queries=self.repository.get_queries()
            for index in similarities_top_matches_desc:
                similar_matches.append(
                    {
                        "query":queries[index],
                        "score":round(float(similarities[index]),2)
                    }
                )

            SearchService.test_FAISS(embeddings,queryEmbedding)

            return similar_matches
        except Exception as e:
            raise

    def test_FAISS(embeddings,query_embeddings):
        print("performing faiss check")
        
        index=ids.get_index(embeddings)

        print(index)

        similarity_score,indices=ids.search_index(index,query_embeddings,2)

        print(similarity_score,indices)

