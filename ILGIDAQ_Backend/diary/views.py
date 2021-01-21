from django.shortcuts import render
from .models import DiaryMeta, DiaryImage, DiaryContent
from .serializers import DiaryMetaSerializer, DiaryImageSerializer, DiaryContentSerializer

from rest_framework import viewsets

###

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

###

# Create your views here.

class DiaryMetaViewset(viewsets.ModelViewSet):
    queryset = DiaryMeta.objects.all()
    serializer_class = DiaryMetaSerializer

class DiaryImageList(generics.ListCreateAPIView):

    queryset = DiaryImage.objects.all()
    serializer_class = DiaryImageSerializer

    def post(self, request):

        serializer = DiaryImageSerializer(data=request.data)

        if serializer.is_valid():

            imageKey = (str(serializer.validated_data['diaryKey'])+"/"+str(serializer.validated_data['imageNum']))
            serializer.validated_data['imageKey'] = imageKey
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiaryImageDetail(APIView):

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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        diaryImage = self.get_object(pk)
        diaryImage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiaryContentList(generics.ListCreateAPIView):

    queryset = DiaryContent.objects.all()
    serializer_class = DiaryContentSerializer

    def post(self, request):

        serializer = DiaryContentSerializer(data=request.data)

        if serializer.is_valid():

            contentKey = str(serializer.validated_data['diaryKey'])
            serializer.validated_data['contentKey'] = contentKey
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiaryContentDetail(APIView):

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