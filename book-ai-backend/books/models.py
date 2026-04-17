from django.db import models

# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    # AI fields
    summary = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)

    # metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.title