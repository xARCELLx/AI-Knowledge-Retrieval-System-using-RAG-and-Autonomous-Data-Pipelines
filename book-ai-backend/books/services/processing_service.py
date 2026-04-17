from books.services.ai_service import generate_summary
from books.services.embedding_service import generate_embedding
from books.services.vector_db import store_embedding
from books.services.utils import chunk_text
from books.services.genre_service import classify_genre


def process_book(book):
    try:
        print(f"\n--- Processing Book: {book.title} ---")

        # 1. Summary
        summary = generate_summary(book.description)
        print("Summary:", summary)

        book.summary = summary

        # 🔥 2. Genre Classification
        text_for_genre = book.summary if book.summary else book.description
        genre = classify_genre(text_for_genre)
        print("Genre:", genre)

        book.genre = genre
        book.save()

        # 3. Chunking
        chunks = chunk_text(book.description)
        print(f"Chunks created: {len(chunks)}")

        # 4. Embeddings
        for i, chunk in enumerate(chunks):
            embedding = generate_embedding(chunk)
            print(f"Embedding {i} generated")

            unique_id = f"{book.id}_{i}"

            store_embedding(
                unique_id=unique_id,
                text=chunk,
                embedding=embedding,
                book_id=book.id
            )

        print("✅ Processing complete\n")

    except Exception as e:
        print(f"❌ ERROR in process_book: {e}")