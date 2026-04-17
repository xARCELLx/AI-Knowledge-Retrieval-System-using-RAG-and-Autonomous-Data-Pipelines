import requests
from books.models import Book
from books.services.processing_service import process_book


def scrape_books(query="fiction", max_results=10):
    url = f"https://openlibrary.org/search.json?q={query}&limit={max_results}"

    try:
        response = requests.get(url, timeout=10)
        print("Status Code:", response.status_code)
    except Exception as e:
        return f"Request failed: {e}"

    if response.status_code != 200:
        return "Failed to fetch books"

    data = response.json()
    docs = data.get("docs", [])

    books_created = 0
    books_processed = 0

    for item in docs:
        try:
            title = item.get("title", "Unknown Title")
            authors = item.get("author_name", ["Unknown Author"])
            description = item.get("first_sentence", "")

            # Normalize formats
            if isinstance(description, list):
                description = description[0]
            elif isinstance(description, dict):
                description = description.get("value", "")

            # 🔥 HARD FALLBACK (CRITICAL FIX)
            if not description or len(description.strip()) < 20:
                description = (
                    f"{title} is a well-known book written by {', '.join(authors)}. "
                    f"It is widely read and appreciated by readers around the world."
                )
            rating = None
            url = f"https://openlibrary.org{item.get('key', '')}"

            # Fix description (sometimes it's dict/list)
            if isinstance(description, list):
                description = description[0]
            elif isinstance(description, dict):
                description = description.get("value", "")

            book, created = Book.objects.get_or_create(
                title=title,
                defaults={
                    "author": ", ".join(authors),
                    "description": description,
                    "rating": rating,
                    "url": url,
                }
            )

            if created:
                print(f"Added: {title}")
                books_created += 1

            if created or not book.summary:
                print(f"Processing AI for: {title}")
                process_book(book)
                books_processed += 1

        except Exception as e:
            print(f"Error processing book: {e}")
            continue

    return f"{books_created} new books added, {books_processed} processed."