from rest_framework import serializers
from .models import DiaryMeta, DiaryImage

class DiaryMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaryMeta
        fields = ('diaryKey', 'writtenDate', 'title', 'openPoint' ,'numView' ,'numLike')

class DiaryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaryImage
        fields = ('diaryKey', 'imageKey', 'image')