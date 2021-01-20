from rest_framework import serializers
from .models import DiaryMeta, 

class DiaryMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaryMeta
        fields = ('diaryKey', 'writtenDate', 'title', 'openPoint' ,'numView' ,'numLike')
