from django.core.management.base import BaseCommand
from books.services.scraper import scrape_books


class Command(BaseCommand):
    help = "Fetch books using Google Books API"

    def add_arguments(self, parser):
        parser.add_argument(
            '--query',
            type=str,
            default='fiction',
            help='Search query'
        )
        parser.add_argument(
            '--max_results',
            type=int,
            default=10,
            help='Number of books to fetch'
        )

    def handle(self, *args, **kwargs):
        query = kwargs['query']
        max_results = kwargs['max_results']

        result = scrape_books(query=query, max_results=max_results)

        self.stdout.write(self.style.SUCCESS(result))