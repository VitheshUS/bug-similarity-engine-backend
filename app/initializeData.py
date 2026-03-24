import json
import model
import numpy as np

def load_data_from_file():
    dataPath='data/bugs.json'
    with open(dataPath) as f:
        texts=json.load(f)

    embeddingPath='data/embedding'
    embeddings=np.load(embeddingPath)

    return texts,embeddings
    
    
