import numpy as np
import json

embeddingPath='data/embedding.npy'

class DataRepository:
    def get_queries(self):
        with open('data/bugs.json') as f:
            bugs=json.load(f)
        return bugs

    def get_embeddings(self):
        embeddings=np.load(embeddingPath)
        return embeddings

    def get_all_data(self):
        return self.get_queries(),self.get_embeddings()

    def add_embeddings(self,embeddings):
        np.save(embeddingPath,embeddings)

    def add_query(self,query):
        with open('data/bugs.json','r') as f:
            bugs=json.load(f)
        bugs.append(query)
        with open('data/bugs.json','w') as f:
            json.dump(bugs,f)