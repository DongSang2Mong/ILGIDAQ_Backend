from django.db import models

# Create your models here.

class UserLoginInfo(models.Model):

    kakaoKey = models.CharField(max_length=100, primary_key=True)

    ####권태환####
    ##kakaoKey는 내가 PK로 써야돼서 임시로 구현해둠.