from django.shortcuts import render
from .models import DiaryMeta, DiaryImage, DiaryContent
from .serializers import DiaryMetaSerializer, DiaryImageSerializer, DiaryContentSerializer

from rest_framework import viewsets
import os

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

###

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

# Create your views here.

class DiaryMetaViewset(viewsets.ModelViewSet):
    queryset = DiaryMeta.objects.all()
    serializer_class = DiaryMetaSerializer

class DiaryImageList(APIView):

    def get(self, request):
        diaryImage = DiaryImage.objects.all()
        serializer = DiaryImageSerializer(diaryImage, many=True)
        return Response(serializer.data)

class DiaryImageWithKey(generics.ListAPIView):

    queryset = DiaryImage.objects.all()
    serializer_class = DiaryImageSerializer

    def get(self, request, dk):

        if len(DiaryMeta.objects.filter(diaryKey=dk))==0 :
            return Response(status=status.HTTP_404_NOT_FOUND)

        images = DiaryImage.objects.filter(diaryKey=dk)
        serializer = DiaryImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, dk):
        
        if len(DiaryMeta.objects.filter(diaryKey=dk))==0 :
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DiaryImageSerializer(data=request.data)

        if serializer.is_valid():

            imageKey = (str(dk)+"/"+str(serializer.validated_data['imageNum']))
            serializer.validated_data['imageKey'] = imageKey
            serializer.validated_data['diaryKey'] = dk
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteFile(pk):
    print("###TESTING###")
    path = os.path.join(BASE_DIR, 'media', pk)
    print(path)

    if os.path.isfile(path):
        os.remove(path)
        return print("######FILE DELETED######")
    else: return print("######CANNOT FIND FILE######")

class DiaryImageDetail(generics.ListAPIView):

    queryset = DiaryImage.objects.all()
    serializer_class = DiaryImageSerializer

    def get_object(self, pk):
        try:
            return DiaryImage.objects.get(pk=pk)
        except DiaryImage.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        diaryImage = self.get_object(pk)
        serializer = DiaryImageSerializer(diaryImage)
        return Response(serializer.data)

    def put(self, request, pk):
        diaryImage = self.get_object(pk)
        serializer = DiaryImageSerializer(diaryImage, data=request.data)
        if serializer.is_valid():
            deleteFile(str(pk))
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        diaryImage = self.get_object(pk)
        deleteFile(str(pk))
        diaryImage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiaryContentList(generics.ListCreateAPIView):

    queryset = DiaryContent.objects.all()
    serializer_class = DiaryContentSerializer

    def post(self, request):

        serializer = DiaryContentSerializer(data=request.data)

        if serializer.is_valid():
            
            try: DiaryMeta.objects.get(diaryKey=serializer.validated_data['diaryKey'])
            except DiaryMeta.DoesNotExist: raise Http404

            contentKey = str(serializer.validated_data['diaryKey'])
            serializer.validated_data['contentKey'] = contentKey
            
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiaryContentDetail(generics.ListCreateAPIView):

    queryset = DiaryContent.objects.all()
    serializer_class = DiaryContentSerializer

    def get_object(self, pk):
        try:
            return DiaryContent.objects.get(pk=pk)
        except DiaryContent.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        diaryContent = self.get_object(pk)
        serializer = DiaryContentSerializer(diaryContent)
        return Response(serializer.data)

    def put(self, request, pk):
        diaryContent = self.get_object(pk)
        serializer = DiaryContentSerializer(diaryContent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        diaryContent = self.get_object(pk)
        diaryContent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)