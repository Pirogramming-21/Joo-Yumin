from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=40)
    release = models.CharField(max_length=30)
    director = models.TextField()
    actor = models.TextField()
    genre = models.TextField()
    score = models.TextField()
    running_time = models.TextField()
    content = models.TextField()
