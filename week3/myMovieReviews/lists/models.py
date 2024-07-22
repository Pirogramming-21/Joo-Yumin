from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=30)
    release = models.IntegerField() 
    director = models.CharField(max_length=100)  
    actor = models.CharField(max_length=100)  
    genre = models.CharField(max_length=50) 
    score = models.FloatField()  
    runningTime = models.IntegerField()  
    content = models.TextField()