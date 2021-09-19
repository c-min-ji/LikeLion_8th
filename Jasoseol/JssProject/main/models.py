from django.db import models

# Create your models here.
class Jasoseol(models.Model):
    title = models.CharField(max_length=50) #제목
    content = models.TextField() #내용
    updated_at = models.DateTimeField(auto_now=True) #날짜 auto_now = True : 현재시간 자동으로

    #def __str__(self):
        #return self.title