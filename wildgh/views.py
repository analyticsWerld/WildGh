import random
from django.shortcuts import render
from .forms import ContactForm
from gallery.models import Gallery
from blog.models import Blog

def home(request):
    albums = random.sample(list(Gallery.objects.all()),9)

    #print([album.image_watermarked for album in albums2])
    #print(albums)
    #print(albums2)
    blogs = Blog.objects.all()[:3]
    #paths = [album.description for album in albums]
    #print(paths)
    return render(request,"wildgh/home.html",{"albums":albums,"blogs":blogs})

def about(request):
    return render(request,"wildgh/about.html")

def contact(request):
    form =  ContactForm(request.POST)
    return render(request,"wildgh/contact.html",{form:form})