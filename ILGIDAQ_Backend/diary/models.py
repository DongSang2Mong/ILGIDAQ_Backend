from django.db import models

# Create your models here.

class DiaryMeta(models.Model):

    #FIELDS#

    diaryKey = models.CharField(max_length=10, primary_key=True)
    writtenDate = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)

    openPoint = models.IntegerField()
    numView = models.IntegerField(default=0)
    numLike = models.IntegerField(default=0)

class DiaryImage(models.Model):

    diaryKey = models.ForeignKey(DiaryMeta, on_delete=models.CASCADE, null=True)
    imageKey = models.CharField(max_length=10, primary_key=True)
    image = models.ImageField(upload_to='', blank = True, null = True)
    