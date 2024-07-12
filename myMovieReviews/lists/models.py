from django.db import models

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=30)
    user = models.CharField(max_length=20)
    content = models.TextField()

