import numpy as np

embeddingPath='data/embedding.npy'
def get_embeddings():
    embeddings=np.load(embeddingPath)
    return embeddings

def put_embeddings(embeddings):
    np.save(embeddingPath,embeddings)