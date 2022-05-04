from unicodedata import category
from django.shortcuts import render
from .models import Gallery

# Create your views here.

def gallery(request):
    
    categories = Gallery.objects.values_list("category",flat=True).distinct()
    
    category_queries = {}
    for category in categories:
        category_queries[category] = Gallery.objects.filter(category=category)
    

    context = {"categories":categories}
    

    context.update(category_queries)
    

    return render(request,"gallery/gallery.html", context)


