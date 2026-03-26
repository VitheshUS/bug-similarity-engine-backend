from app.config import K,THRESHOLD
from app.domain.model.searchService.queryScore import QueryScore

class SearchService:
    def __init__(self,repository,index,embedding_service):
        self.repository=repository
        self.index=index
        self.embedding_service=embedding_service

    def getMatches(self,query:str):
        try:
            queryEmbedding=self.embedding_service.generate_embedding(query).reshape(1,-1)

            similarity_score,indices=self.index.search_index(queryEmbedding,K)

            similar_matches=[]

            queries=self.repository.get_queries()

            for index in range(len(indices)):
                if similarity_score[index]>THRESHOLD:
                    continue

                similar_matches.append(
                            QueryScore(
                                queries[indices[index]],
                                round(float(similarity_score[index]),2)
                            ).to_dict()
                        )

            return similar_matches
        except Exception as e:
            raise

