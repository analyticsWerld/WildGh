from socket import timeout
from sqlite3 import connect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core import mail
from django.http import HttpResponse
from .models import Accounts
from .forms import SignUpForm, LogInForm
from django.conf import settings

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/activation_email.html', {
                'user':user, 
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your account.'
            to_email = form.cleaned_data.get('email')
            sender = settings.EMAIL_HOST_USER
            mail.send_mail(mail_subject, message,sender,[to_email,])
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()   
    return render(request, 'accounts/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Accounts.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Accounts.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')
        #return render(request, 'account/account_activation_email.html', context)

def log_in(request):
    error = False
    #if request.user.is_authenticated:
    #    return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)  
                return redirect('home')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'accounts/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('login'))