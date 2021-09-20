from django.shortcuts import render, redirect
from .forms import CreateBlog
from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blogmain(request):
    blogs = Blog.objects.all()

    return render(request, 'blogmain.html',{'blogs':blogs})

def createblog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('blogmain')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'createblog.html', {'form': form})
 
    # form = CreateBlog()
    # return render(request, 'createblog.html', {'form': form})