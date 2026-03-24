from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "App crashes when clicking login",
    "Login button causes application crash",
    "Database connection timeout error"
]

embeddings = model.encode(sentences)

query=['cant store data']

query_embedding=model.encode(query)


# Compare all sentences
similarity_matrix = cosine_similarity(query_embedding,embeddings)[0]

#for the top k
k=2
threshold=0.6
topK=similarity_matrix.argsort()[-k:][::-1]

print('The top matching sentences are')
for i in topK:
    if similarity_matrix[i]>threshold:
        print(sentences[i])

