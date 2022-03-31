from django.shortcuts import render
from .models import Gallery

# Create your views here.

def gallery(request):
    galleries = Gallery.objects.all()
    return render(request,"gallery/gallery.html", {"galleries":galleries})


