# form & import 잘 확인
from django.shortcuts import render,get_object_or_404, redirect
from .models import Post, Comment
from faker import Faker
from django.utils import timezone
from .forms import PostForm


# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def create10(request):
    ifake = Faker()
    for i in range(10):
        post = Post()
        post.title = ifake.name()
        post.body = ifake.sentence()
        post.pub_date = timezone.datetime.now()
        post.save()
    return redirect('/')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            # 나는 왜.....뒤에 슬래시(/)하나 더 쳐줘야 나오지..^^?
            return redirect('/' + str(post.id) + '/')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form': form})
    
    #form = PostForm()
    #return render(request, 'new.html', {'form': form})

def edit(request, post_id):
    #현재 게시물의 정보 얻어오기
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post) #인스턴스는 수정하려는 글 post모델의 객체 정보 가져오는 거
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/' + str(post.id) + '/')
    else:
        form = PostForm(instance=post)
    return render(request, 'new.html', {'form': form})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/')

def comments_create(request, post_id):
    post = Post.objects.get(pk=post_id)
    content = request.POST.get('content')
    #댓글 생성 
    comment = Comment(post=post, content=content)
    comment.save()
    return redirect('/' + str(post.id) + '/')

def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    
    return redirect('/' + str(post_id) + '/')

def comments_update(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('/' + str(post_id) + '/')
    else:
        return render(request, 'comments_update.html', {'post':post, 'comment': comment})