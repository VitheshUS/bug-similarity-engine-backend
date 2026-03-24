#Sentence traformers to embed the sentences and get a vector that reprsent that senetence in a semenatic space
#This emebed not only checks the words in the sentence but also the pattern in it
from sentence_transformers import SentenceTransformer
#import data_repository as dr

model=SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    embedding=model.encode(text)
    return embedding

def save_embedding(text):
    get_embedding(text)
