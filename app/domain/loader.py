import numpy as np
import json

class Loader:
    def __init__(self,embedding_service):
        self.embedding_service=embedding_service

    def load_data(self):
        print("Loading data...",self.embedding_service)
        dataPath='data/bugs.json'
        with open(dataPath) as f:
            texts=json.load(f)

        embedding = self.embedding_service.generate_embedding(texts)

        embeddingPath = 'data/embedding.npy'
        np.save(embeddingPath, embedding)

    def clear_data(self):
        # Clear the data from the repository
        self.embedding_service.data_store.clear_embeddings()