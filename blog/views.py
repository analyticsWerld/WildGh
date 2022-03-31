from django.shortcuts import render
from .models import Blog

# Create your views here.

def blogs(request):
    blogs = Blog.objects.all()
    return render(request,"blog/blogs.html",{"blog":blog})


def blog(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,"blog/blog.html",{"blog":blog})