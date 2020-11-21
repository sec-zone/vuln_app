from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    posts = Blog.objects.all()
    lastseen = request.COOKIES.get('lastseen')
    return render(request, 'blog.html', locals())

def post(request, id):
    post = Blog.objects.get(id=id)
    lastseen = request.COOKIES.get('lastseen')
    return render(request, 'post.html', locals())
