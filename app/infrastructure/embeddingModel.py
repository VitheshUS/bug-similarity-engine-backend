from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model):
        self.model = model

    def encode(self, text):
        return self.model.encode(text)