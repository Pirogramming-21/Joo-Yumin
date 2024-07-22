from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 다른 모델에 대한 링크
    title = models.CharField(max_length=200) # 글자 수가 제한된 텍스트 정의 시 사용
    text = models.TextField() # 글자 수에 제한이 없는 긴 텍스트 정의
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField( # 날짜와 시간
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title