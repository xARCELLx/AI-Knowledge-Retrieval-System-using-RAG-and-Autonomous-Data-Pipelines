from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.services.rag_service import ask_question
from books.services.recommendation_service import recommend_books
from books.services.scraper import scrape_books


@api_view(["POST"])
def fetch_books(request):
    try:
        # You can make this dynamic later
        query = request.data.get("query", "harry potter")
        max_results = int(request.data.get("max_results", 5))

        result = scrape_books(query=query, max_results=max_results)

        return Response({
            "message": "Books fetched successfully",
            "result": result
        })

    except Exception as e:
        return Response({"error": str(e)}, status=500)


# ✅ GET /api/books/
@api_view(["GET"])
def list_books(request):
    books = Book.objects.all().order_by("-id")
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# ✅ GET /api/books/<id>/
@api_view(["GET"])
def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)


# ✅ GET /api/recommend/<id>/
@api_view(["GET"])
def recommend_view(request, book_id):
    books = recommend_books(book_id)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# ✅ POST /api/ask/
@api_view(["POST"])
def ask_view(request):
    question = request.data.get("question")

    if not question:
        return Response({"error": "Question is required"}, status=400)

    result = ask_question(question)

    return Response(result)

