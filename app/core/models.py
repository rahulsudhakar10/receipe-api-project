from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, \
                                       PermissionsMixin


class UserManger(BaseUserManager):

    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('Email was not present')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff= True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(max_length=234,unique=True)
    name = models.CharField(max_length=234)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManger()

    USERNAME_FIELD= 'email'