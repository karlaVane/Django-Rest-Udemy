from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
