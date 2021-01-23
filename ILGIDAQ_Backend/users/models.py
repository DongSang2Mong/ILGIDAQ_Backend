from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.


##class UserLoginInfo(models.Model):

  ##  kakaokey = models.CharField(max_length=100, primary_key=True)

    ####권태환####
    ##kakaoKey는 내가 PK로 써야돼서 임시로

    # 구현해둠.


class UserManager(BaseUserManager):
    def create_user(self, kakaoid, password=None):
        if kakaoid is None:
            raise TypeError('Need to type kakaoid')

        user = self.model(kakaoid=kakaoid)
        user.set_password('1111')
        user.save()
        return user

    def create_superuser(self, kakaoid, password=None):
        if kakaoid is None:
            raise TypeError('Need to type kakaoid')
        user = self.model(kakaoid=kakaoid, password=password)
        user.set_password(1111)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    kakaoid = models.CharField(max_length=100, primary_key=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'kakaoid'

    objects = UserManager()

    def __str__(self):
        return self.kakaoid

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)

        }
