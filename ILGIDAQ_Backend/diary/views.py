from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DiaryMetaSerializer
from .models import DiaryMeta

# Create your views here.

class DiaryMetaViewset(viewsets.ModelViewSet):
    queryset = DiaryMeta.objects.all()
    serializer_class = DiaryMetaSerializer