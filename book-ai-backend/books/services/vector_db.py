import chromadb

# ✅ Persistent client (THIS IS THE FIX)
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="books")


def store_embedding(unique_id, text, embedding, book_id):
    collection.add(
        ids=[str(unique_id)],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{"book_id": book_id}]
    )


def query_similar(query_embedding, n_results=3):
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )