from django.db import models
from apps.devTools.models import DevTool


# Create your models here.
class Post(models.Model):
    title = models.CharField('제목', max_length=24)
    content = models.CharField('내용', max_length=24)
    interest = models.IntegerField('관심도', default=0)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')

    devtool = models.ForeignKey(DevTool, on_delete=models.SET_NULL, verbose_name='예상 개발툴', null=True, blank=True)

    # 생성 시각, 수정 시각
    created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일', auto_created=True, auto_now=True)

    SORT_CHOICE = [
        ('star', '찜하기순'),
        ('name', '이름순'),
        ('register', '등록순'),
        ('new', '최신순'),
    ]
