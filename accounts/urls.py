from django.urls import path
from .views import signup, log_in, log_out,activate

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activate/<uidb64>/<token>/',  
        activate, name='activate'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
]