from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(query_embedding, embeddings):
    try:
        return cosine_similarity(query_embedding, embeddings)[0]
    except Exception as e:
        raise