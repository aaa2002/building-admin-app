import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,UserManager
from django.db import models
from django.utils import timezone

# Create your models here.

class CustomUserManager(UserManager):

    def _create_user(self,name,email,password,**extra_fields):
        if not email:
            raise ValueError("Not a valid e-mail address")
        
        email = self.normalize_email(email)
        name = self.name
        user = self.model(email=email,name=name,**extra_fields)
        user.set_password(password)
        
        user.save(using=self.db)
        
        return user
    
    def create_user(self,name = None, email=None, password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(name, email, password, **extra_fields)
    
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(name, email, password, **extra_fields)    

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True,default='', blank=True)
    name = models.CharField(max_length=255,blank=True,default='',null=True)
    
    is_active=models.BooleanField(default = True)
    is_staff=models.BooleanField(default = False)
    is_superuser=models.BooleanField(default = False)
    
    objects=CustomUserManager()

    USERNAME_FIELD='email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=[]