from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from faker import Faker

from .models import *

# Create your views here.

def home(request):
    posts = Post.objects
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    posts_num = paginator.get_page(page)
    return render(request, 'home.html', {'posts':posts_num, 'blogs':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request):
    return render(request, 'new.html')

myfake = Faker('ko_KR')
def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    # 랜덤으로 제목과 글 쓰기
    #post.title = myfake.name()
    #post.body = myfake.sentence()
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/' + str(post.id))

def delete(request, post_id):
    post_num = get_object_or_404(Post, pk=post_id)
    post_num.delete()
    return redirect('/')
