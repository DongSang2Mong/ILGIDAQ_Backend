from django.db import models
import uuid

# Create your models here.

class UserLoginInfo(models.Model):

    #FIELDS#

    userKey = models.CharField(max_length=40, default=uuid.uuid4, primary_key=True, editable=False, )

    ## 이 부분 알아서 편집해서 쓰셈 ##

    kakao_id = models.CharField(max_length=40, default='')
    acceseToken = models.CharField(max_length=40, default='')
    refreshToken = models.CharField(max_length=40, default='')
    tokenDue = models.CharField(max_length=40, default='')

    ##

class UserProfile(models.Model):

    userKey = models.CharField(max_length=40, null=False)
    profileKey = models.CharField(max_length=40, primary_key=True, editable=False)
    tempContent = models.TextField(max_length=4000)