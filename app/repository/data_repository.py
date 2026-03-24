import numpy as np
import json

embeddingPath='data/embedding.npy'

def get_queries():
    with open('data/bugs.json') as f:
        bugs=json.load(f)
    return bugs

def get_embeddings():
    embeddings=np.load(embeddingPath)
    return embeddings

def get_all_data():
    return get_queries(),get_embeddings()

def put_embeddings(embeddings):
    np.save(embeddingPath,embeddings)