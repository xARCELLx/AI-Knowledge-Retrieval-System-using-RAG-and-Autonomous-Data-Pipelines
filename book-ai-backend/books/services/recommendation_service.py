from books.models import Book
from books.services.embedding_service import generate_embedding
from books.services.vector_db import query_similar


def recommend_books(book_id):
    try:
        book = Book.objects.get(id=book_id)

        # Use summary or description
        text = book.summary if book.summary else book.description

        if not text:
            return []

        # Generate embedding for this book
        embedding = generate_embedding(text)

        # Query similar chunks
        results = query_similar(embedding, n_results=5)

        metadatas = results.get("metadatas", [[]])[0]

        # Extract book_ids (excluding current book)
        similar_ids = list(set(
            m["book_id"] for m in metadatas if m["book_id"] != book.id
        ))

        # Fetch books
        return Book.objects.filter(id__in=similar_ids)

    except Exception as e:
        print("Recommendation error:", e)
        return []