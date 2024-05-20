from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password=None):
        user=user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    email=  models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    bio =models.TextField(max_length=700, blank=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)


    objects = UserAccountManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']


    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email









