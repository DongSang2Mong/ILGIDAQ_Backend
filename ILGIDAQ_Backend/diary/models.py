from django.db import models
import uuid

# Create your models here.

class DiaryMeta(models.Model):

    #FIELDS#

    diaryKey = models.CharField(max_length=40, default=uuid.uuid4, primary_key=True, editable=False, )
    writtenDate = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)

    numImage = models.PositiveIntegerField(default=0)

    openPoint = models.PositiveIntegerField(default=0)
    numView = models.PositiveIntegerField(default=0, editable=False)
    numLike = models.PositiveIntegerField(default=0, editable=False)

class DiaryImage(models.Model):

    diaryKey = models.CharField(max_length=40)
    imageNum = models.PositiveIntegerField(default=0)
    imageKey = models.CharField(max_length=40, primary_key=True, editable=False)
    image = models.ImageField(upload_to='', blank = True, null = True)

class DiaryContent(models.Model):

    diaryKey = models.CharField(max_length=40)
    contentKey = models.CharField(max_length=40, primary_key=True, editable=False)
    content = models.TextField(max_length=4000)
    