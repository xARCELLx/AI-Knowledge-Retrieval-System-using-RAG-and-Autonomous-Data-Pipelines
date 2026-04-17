from rest_framework import serializers
from .models import Book

from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "summary",
            "rating",
            "url",
            "genre", 
        ]