import time

class InsertService:
    def __init__(self,repository,index,embedding_service,logger):
        self.repository=repository
        self.index=index
        self.embedding_service=embedding_service
        self.logger=logger

    def addQuery(self,query:str):
        try:
            start_time=time.time() #logging the start time of the insert operation

            query_embedding=self.embedding_service.generate_embedding(query).reshape(1,-1)

            query_embedding_end_time=time.time() #logging the time taken to generate the embedding for the query

            self.repository.add_query(query)

            self.repository.add_embeddings(query_embedding)

            add_query_end_time=time.time() #logging the time taken to add the query to the repository

            self.index.add_embeddings(query_embedding)

            index_update_end_time=time.time() #logging the time taken to update the index with the new query embedding

            # Logging the time taken for the entire insert operation, as well as the time taken for each individual step 
            self.logger.info(
                f"Insert operation completed in {round(time.time()-start_time,2)} seconds | "
                f"Query embedding time: {round(query_embedding_end_time-start_time,2)} seconds | "
                f"Add query time: {round(add_query_end_time-query_embedding_end_time,2)} seconds | "
                f"Index update time: {round(index_update_end_time-add_query_end_time,2)} seconds"
            )
        except Exception as e:
            raise