import numpy as np
import json
from app.service import embedding_service as es

dataPath='data/bugs.json'
with open(dataPath) as f:
    texts=json.load(f)

embedding=es.generate_embedding(texts)

embeddingPath='data/embedding'

np.save(embeddingPath,embedding)