from django.urls import path
from .views import list_books,book_detail,recommend_view,ask_view,fetch_books

urlpatterns = [
   path("books/", list_books),
    path("books/<int:book_id>/", book_detail),
    path("recommend/<int:book_id>/", recommend_view),
    path("ask/", ask_view),
    path("fetch-books/", fetch_books),
]