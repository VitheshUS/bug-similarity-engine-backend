from app.utils import similarity as similarity_check
from app.infrastructure import index as ids
from app.config import K,THRESHOLD

class SearchService:
    def __init__(self,repository,index,embedding_service):
        self.repository=repository
        self.index=index
        self.embedding_service=embedding_service

    def getMatches(self,query:str):
        try:
            queryEmbedding=self.embedding_service.generate_embedding(query).reshape(1,-1)

            similarity_score,indices=ids.search_index(self.index,queryEmbedding,K)

            similar_matches=[]

            queries=self.repository.get_queries()

            for index in range(len(indices)):
                similar_matches.append(
                    {
                        "query":queries[indices[index]],
                        "score":round(float(similarity_score[index]),2)
                    }
                )

            return similar_matches
        except Exception as e:
            raise

