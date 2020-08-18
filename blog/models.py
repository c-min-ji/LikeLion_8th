from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    #제목 목차에서 보이게 하는 함수
    def __str__(self):
        return self.title
    #미리보기
    def summary(self):
        return self.body[:100]