# from django.shortcuts import render
# from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import ApiSerializer
from .models import Post
# Create your views here.
class ApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ApiSerializer