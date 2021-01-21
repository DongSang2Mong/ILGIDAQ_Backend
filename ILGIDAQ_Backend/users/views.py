from django.shortcuts import render
from .models import UserLoginInfo, UserProfile
from .serializers import UserLoginInfoSerializer, UserProfileSerializer

from rest_framework import viewsets

###

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

###

### 얘도 ###

class UserLoginInfoViewset(viewsets.ModelViewSet):

    queryset = UserLoginInfo.objects.all()
    serializer_class = UserLoginInfoSerializer

###

class UserProfileView(generics.ListCreateAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def post(self, request):

        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():

            profileKey = str(serializer.validated_data['userKey'])
            serializer.validated_data['profileKey'] = profileKey
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)