from django.db import models
import uuid

def image_path(instance, filename):
    return f'{instance.diaryKey}/{instance.imageNum}'


# Create your models here.

class DiaryMeta(models.Model):

    #FIELDS#

    diaryKey = models.CharField(max_length=36, default=uuid.uuid4, primary_key=True, editable=False, )
    writtenDate = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50, null=False)

    numImage = models.PositiveIntegerField(null=False)

    openPoint = models.PositiveIntegerField(default=0)
    numView = models.PositiveIntegerField(default=0, editable=False)
    numLike = models.PositiveIntegerField(default=0, editable=False)


class DiaryImage(models.Model):

    diaryKey = models.CharField(max_length=36, null=False, editable=False)
    imageNum = models.PositiveIntegerField(null=False)
    imageKey = models.CharField(max_length=36, primary_key=True, editable=False)
    image = models.ImageField(upload_to=image_path, blank = True, null = True)

class DiaryContent(models.Model):

    diaryKey = models.CharField(max_length=36, null=False)
    contentKey = models.CharField(max_length=36, primary_key=True, editable=False)
    content = models.TextField(max_length=4000, null=False)
    