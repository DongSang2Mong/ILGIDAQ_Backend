from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DiaryMetaSerializer, DiaryImageSerializer
from .models import DiaryMeta, DiaryImage

# Create your views here.

class DiaryMetaViewset(viewsets.ModelViewSet):
    queryset = DiaryMeta.objects.all()
    serializer_class = DiaryMetaSerializer

class DiaryImageViewset(viewsets.ModelViewSet):
    queryset = DiaryImage.objects.all()
    serializer_class = DiaryImageSerializer