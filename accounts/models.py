from re import M
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

gender_options = [("MALE","Male"),("FEMALE","Female")]
# Create your models here.
class AccountsManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given username and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        #TODO : Modify this to prevent superuser status from being nullified
        if extra_fields.get("is_staff") is True or extra_fields.get("is_superuser") is True:
            pass
        else:
            extra_fields["is_staff"] =  False
            extra_fields["is_superuser"] =  False
            
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)


class Accounts(AbstractUser):

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    username = None
    photo = models.ImageField(upload_to='members/%Y',blank=True)
    address = models.TextField(max_length=250)
    gender = models.CharField(choices=gender_options, max_length=250,blank=True )
    mobile_number = models.CharField(max_length=15,blank=True)
    email = models.EmailField("email address",max_length=100,unique=True)


    objects = AccountsManager()

    def __str__(self):
        return f'Profile for user {self.username}'


class Contact(models.Model):
    fullname = models.CharField(max_length=200,blank=True, null=True)
    email = models.EmailField(max_length=300,blank=True, null=True)
    message = models.CharField(max_length=700,blank=True, null=True)

