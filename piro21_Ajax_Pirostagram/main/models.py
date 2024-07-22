from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField(default=0)
    comment = models.TextField()
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    created_date = models.DateTimeField('작성일', default=timezone.now)
