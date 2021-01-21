from rest_framework import serializers
from .models import DiaryMeta, DiaryImage, DiaryContent

class DiaryMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaryMeta
        fields = ('diaryKey', 'writtenDate', 'title', 'numImage', 'openPoint' ,'numView' ,'numLike')

class DiaryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaryImage
        fields = ('diaryKey', 'imageNum', 'imageKey', 'image')

class DiaryContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaryContent
        fields = ('diaryKey', 'contentKey', 'content')