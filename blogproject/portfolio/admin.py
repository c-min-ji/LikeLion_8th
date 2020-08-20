from django.contrib import admin
from .models import Portfolio

# Register your models here.

#어드민 사이트에 Portfolio라는 페이지를 등록한다.
admin.site.register(Portfolio)