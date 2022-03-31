from django.urls import path
from .views import blog,blogs

urlpatterns = [
    path('blogs/', blogs, name='blogs'),
    path('blogs/<int:id>', blog, name='blog'),
]