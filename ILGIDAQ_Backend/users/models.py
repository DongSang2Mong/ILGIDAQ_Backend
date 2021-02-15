from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django_uuid_upload import upload_to_uuid
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
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


class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        user_pk = models.IntegerField(blank=True)
        nickname = models.CharField(max_length=40)
        profileimg = models.ImageField(default='default.jpg', upload_to=upload_to_uuid('profile_pic'))
        statusmsg = models.TextField(blank=True)
        numFollower = models.PositiveIntegerField(default=0, editable=True)
        numFollowing = models.PositiveIntegerField(default=0, editable=True)
        valPoints = models.PositiveIntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.kakaoid)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


