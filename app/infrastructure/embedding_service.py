#Sentence traformers to embed the sentences and get a vector that reprsent that senetence in a semenatic space
#This emebed not only checks the words in the sentence but also the pattern in it

class EmbeddingService:
    def __init__(self,model,data_store):
        self.model=model
        self.data_store=data_store

    def generate_embedding(self, text):
        embedding=self.model.encode(text)
        return embedding

    def save_embedding(self,text):
        embedding=self.generate_embedding(text)
        self.data_store.put_embeddings(embedding)

