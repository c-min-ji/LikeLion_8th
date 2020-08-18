from django.contrib import admin
from .models import Post

# Register your models here.

#어드민 사이트에 Post라는 페이지를 등록한다.
admin.site.register(Post)