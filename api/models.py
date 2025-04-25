from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, null=True , blank=True)
    download_link = models.URLField(null=True, blank=True)
    cover_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
