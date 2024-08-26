from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'"{self.text}" - {self.author}'
