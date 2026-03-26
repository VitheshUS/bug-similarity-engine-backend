from app.config import K,THRESHOLD
from app.domain.model.searchService.queryScore import QueryScore
import time

class SearchService:
    def __init__(self,repository,index,embedding_service,logger):
        self.repository=repository
        self.index=index
        self.embedding_service=embedding_service
        self.logger=logger

    def getMatches(self,query:str):
        try:
            start_time=time.time() #logging the start time of the search operation

            queryEmbedding=self.embedding_service.generate_embedding(query).reshape(1,-1)

            query_embedding_end_time=time.time() #logging the time taken to generate the embedding for the query

            similarity_score,indices=self.index.search_index(queryEmbedding,K)

            similarity_score_end_time=time.time() #logging the time taken to search the index for similar matches

            similar_matches=[]

            queries=self.repository.get_queries()

            get_queries_end_time=time.time() #logging the time taken to get the queries from the repository

            for index in range(len(indices)):
                if similarity_score[index]>THRESHOLD:
                    continue

                similar_matches.append(
                            QueryScore(
                                queries[indices[index]],
                                round(float(similarity_score[index]),2)
                            ).to_dict()
                        )

            # Logging the time taken for the entire search operation, as well as the time taken for each individual step 
            self.logger.info(
                f"Search operation completed in {round(time.time()-start_time,2)} seconds | "
                f"Query embedding time: {round(query_embedding_end_time-start_time,2)} seconds | "
                f"Index search time: {round(similarity_score_end_time-query_embedding_end_time,2)} seconds | "
                f"Get queries time: {round(get_queries_end_time-similarity_score_end_time,2)} seconds"
            )

            return similar_matches
        except Exception as e:
            raise

