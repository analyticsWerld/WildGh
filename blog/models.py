from django.db import models
#from accounts.models import Accounts

# Create your models here.
class Blog(models.Model):

    blogger = models.TextField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    blog = models.TextField(max_length=10000)
