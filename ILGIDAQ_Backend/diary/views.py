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

class aboutDiaryMeta(generics.ListAPIView):

    queryset= DiaryMeta.objects.all()
    serializer_class = DiaryMetaSerializer

class DiaryMetaList(aboutDiaryMeta):

    def get(self,request):
        diaryMeta = DiaryMeta.objects.all()
        serializer = DiaryMetaSerializer(diaryMeta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        
        serializer = DiaryMetaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiaryMetaDetail(aboutDiaryMeta):

    def objectChk(self, dk):
        if len(DiaryMeta.objects.filter(diaryKey=dk))==0: return False
        else: return True

    def get(self, request, dk):
        chk = self.objectChk(dk)
        if chk:
            diaryMeta = DiaryMeta.objects.get(diaryKey=dk)
            serializer = DiaryMetaSerializer(diaryMeta)
            return Response(serializer.data)
        else:
            return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, dk):
        chk = self.objectChk(dk)
        if chk:
            diaryMeta = DiaryMeta.objects.get(diaryKey=dk)
            serializer = DiaryMetaSerializer(diaryMeta, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, dk):
        chk = self.objectChk(dk)
        if chk:
            diaryMeta = DiaryMeta.objects.get(diaryKey=dk)
            diaryMeta.delete()
            return Response(data="diary :"+dk+" is deleted", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)

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
            return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)

        images = DiaryImage.objects.filter(diaryKey=dk)
        serializer = DiaryImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, dk):
        
        if len(DiaryMeta.objects.filter(diaryKey=dk))==0 :
            return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)

        serializer = DiaryImageSerializer(data=request.data)

        if serializer.is_valid():
            
            imagenum = serializer.validated_data['imageNum']
            chkstring = dk + "/" + str(imagenum)
            if len(DiaryImage.objects.filter(imageKey=chkstring))==1:
                return Response(data="diaryImage: "+chkstring+" is already exist", status=status.HTTP_400_BAD_REQUEST)

            diary = DiaryMeta.objects.get(diaryKey=dk)
            if serializer.validated_data['imageNum']>diary.numImage:
                return Response(data="diary: "+dk+" - 's images cannot over "+str(diary.numImage), status=status.HTTP_400_BAD_REQUEST)
            

            imageKey = (str(dk)+"/"+str(serializer.validated_data['imageNum']))
            serializer.validated_data['imageKey'] = imageKey
            serializer.validated_data['diaryKey'] = dk
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteFile(pk):
    path = os.path.join(BASE_DIR, 'media', pk)
    print(path)

    if os.path.isfile(path):
        os.remove(path)
        return print("######FILE DELETED######")
    else: return print("######CANNOT FIND FILE######")

class DiaryImageDetail(generics.ListAPIView):

    queryset = DiaryImage.objects.all()
    serializer_class = DiaryImageSerializer

    def metaChk(self, dk):
        if len(DiaryMeta.objects.filter(diaryKey=dk))==0: return False
        else: return True

    def imgChk(self, dk, ik):
        imageKey = dk+"/"+ik
        if len(DiaryImage.objects.filter(imageKey=imageKey))==0: return False
        else: return True

    def get(self, request, dk, ik):

        chk = self.metaChk(dk)
        if chk==False: return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)

        chk = self.imgChk(dk, ik)
        if chk==False: return Response(data="Cannot Find image: "+dk+"/"+ik+" in DB", status=status.HTTP_404_NOT_FOUND)

        imageKey = dk+"/"+ik
        diaryImage = DiaryImage.objects.get(imageKey=imageKey)
        serializer = DiaryImageSerializer(diaryImage)
        return Response(serializer.data)

    def put(self, request, dk, ik):

        chk = self.metaChk(dk)
        if chk==False: return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)

        chk = self.imgChk(dk, ik)
        if chk==False: return Response(data="Cannot Find image: "+dk+"/"+ik+" in DB", status=status.HTTP_404_NOT_FOUND)

        imageKey = dk+"/"+ik
        diaryImage = DiaryImage.objects.get(imageKey=imageKey)
        serializer = DiaryImageSerializer(diaryImage, data=request.data)
        if serializer.is_valid():
            deleteFile(str(imageKey))
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, dk, ik):
        
        chk = self.metaChk(dk)
        if chk==False: return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)

        chk = self.imgChk(dk, ik)
        if chk==False: return Response(data="Cannot Find image: "+dk+"/"+ik+" in DB", status=status.HTTP_404_NOT_FOUND)

        imageKey = dk+"/"+ik
        diaryImage = DiaryImage.objects.get(imageKey=imageKey)
        deleteFile(str(imageKey))
        diaryImage.delete()
        return Response(data="image: "+imageKey+" is deleted", status=status.HTTP_204_NO_CONTENT)

class DiaryContentList(generics.ListAPIView):

    queryset = DiaryContent.objects.all()
    serializer_class = DiaryContentSerializer

class DiaryContentDetail(generics.ListCreateAPIView):

    queryset = DiaryContent.objects.all()
    serializer_class = DiaryContentSerializer

    def metaChk(self, dk):
        if len(DiaryMeta.objects.filter(diaryKey=dk))==0: return False
        else: return True

    def get(self, request, dk):

        chk = self.metaChk(dk)
        if chk==False: return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)
        if len(DiaryContent.objects.filter(contentKey=dk))==0: return Response(data="diary: "+dk+" - Content is not created.", status=status.HTTP_400_BAD_REQUEST)

        diaryContent = DiaryContent.objects.get(contentKey=dk)
        serializer = DiaryContentSerializer(diaryContent)
        return Response(serializer.data)

    def post(self, request, dk):

        chk = self.metaChk(dk)
        if chk==False: return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)
        
        serializer = DiaryContentSerializer(data=request.data)

        if serializer.is_valid():
            
            serializer.validated_data['contentKey'] = dk
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, dk):

        chk = self.metaChk(dk)
        if chk==False: return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)
        if len(DiaryContent.objects.filter(contentKey=dk))==0: return Response(data="diary: "+dk+" - Content is not created.", status=status.HTTP_400_BAD_REQUEST)

        diaryContent = DiaryContent.objects.get(contentKey=dk)
        serializer = DiaryContentSerializer(diaryContent, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, dk):

        chk = self.metaChk(dk)
        if chk==False: return Response(data="Cannot Find diary: "+dk+" in DB", status=status.HTTP_404_NOT_FOUND)
        if len(DiaryContent.objects.filter(contentKey=dk))==0: return Response(data="diary: "+dk+" - Content is not created.", status=status.HTTP_400_BAD_REQUEST)

        diaryContent = DiaryContent.objects.get(contentKey=dk)
        diaryContent.delete()
        return Response(data="content: "+dk+" is deleted", status=status.HTTP_204_NO_CONTENT)