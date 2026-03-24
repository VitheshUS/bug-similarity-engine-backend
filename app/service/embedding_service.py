#Sentence traformers to embed the sentences and get a vector that reprsent that senetence in a semenatic space
#This emebed not only checks the words in the sentence but also the pattern in it
from sentence_transformers import SentenceTransformer
from app.repository import data_repository as data_store

model=SentenceTransformer('all-MiniLM-L6-v2')

def generate_embedding(text):
    embedding=model.encode(text)
    return embedding

def save_embedding(text):
    embedding=generate_embedding(text)
    data_store.put_embeddings(embedding)

