from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, userid, password=None):
        if userid is None:
            raise TypeError('User ID required')
        if User.objects.filter(userid=userid).exists():
            raise TypeError('Already existing User ID')

        user = self.model(userid=userid)
        user.set_password('1111')
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    userid = models.CharField(max_length=250, unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'userid'

    objects = UserManager()

    def __str__(self):
        return self.userid

    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


