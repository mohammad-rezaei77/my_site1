from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager


#create Your managers

class UserManager(BaseUserManager):
    def create_user(self,email,username,name,phone,password):
        if not email:
            raise ValueError('plz Email')
        if not username:
            raise ValueError('plz username')
        if not phone:
            raise ValueError('plz phone')

        user = self.model(email = self.normalize_email(email),username=username,name=name,phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,name,phone,password):
        user = self.create_user(email,username,name,phone,password)
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=258)
    email = models.EmailField(unique=True)
    phone = models.IntegerField() 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name', 'phone']
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin