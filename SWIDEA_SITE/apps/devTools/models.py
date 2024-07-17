from django.db import models

# Create your models here.
class DevTool(models.Model):
    name = models.CharField(max_length=24)
    kind = models.CharField(max_length=24)
    content = models.CharField(max_length=100)
    