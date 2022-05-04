import random
from django.shortcuts import render,redirect
from .forms import ContactForm
from gallery.models import Gallery
from blog.models import Blog
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError
from .local_settings import EMAIL_HOST_USER as admin

def home(request):
    albums = random.sample(list(Gallery.objects.all()),9)
    blogs = Blog.objects.all()[:3]
    

    return render(request,"wildgh/home.html",{"albums":albums,"blogs":blogs})

def about(request):
    return render(request,"wildgh/about.html")

def contact(request):
    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            try:
                send_mail(subject,message,sender,[admin])
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            
            return HttpResponse("success")
            #return render(request,"wildgh/contact.html",{"form":form,"message":"Mail successfully sent."})
        
    else:
        form =  ContactForm()

    return render(request,"wildgh/contact.html",{"form":form})


def success(request):
    return HttpResponse('Mail successfully sent.')