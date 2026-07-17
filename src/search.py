from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def search(collection, query, n_results=3):
    """
    Search for the most similar chunks.
    """
    #convert the questions(input) into vectors
    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results,
    )

    return results