from django.shortcuts import render
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Profile
import requests
import json
from django.http import Http404
from rest_framework import permissions
from .permissions import IsOwner
# Create your views here.


class LoginAPIView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    serializer_class1 = LoginSerializer

    def post(self, request):
        kakaouserid = request.data['kakaoid']

        datas = {
            'target_id_type': 'user_id',
            'target_id': kakaouserid
        }
        headers = {'Authorization': 'KakaoAK bd12d8ffd213727918a549f8aa789e8c'}

        profile_request = requests.post("https://kapi.kakao.com/v2/user/me",
                                        headers=headers,
                                        data=datas)

        if profile_request.status_code == 200:

            if not User.objects.filter(kakaoid=request.data['kakaoid']).exists():

                user = request.data
                serializer = self.serializer_class(data=user)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                user_data = serializer.data

                user = User.objects.get(kakaoid=user_data['kakaoid'])
                token = RefreshToken.for_user(user)

                serializer1 = self.serializer_class1(data=request.data)
                serializer1.is_valid(raise_exception=True)

                return Response(serializer1.data, status=status.HTTP_200_OK)

            if User.objects.filter(kakaoid=request.data['kakaoid']).exists():

                serializer1 = self.serializer_class1(data=request.data)
                serializer1.is_valid(raise_exception=True)

                return Response(serializer1.data, status=status.HTTP_200_OK)

        if not profile_request.status_code == 200:

            raise Http404


class ProfileUpdateAPI(generics.UpdateAPIView, mixins.ListModelMixin):
    lookup_field = "user_pk"
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProfileListAPI(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ProfileDetailAPI(generics.RetrieveUpdateAPIView):
    lookup_field = "user_pk"
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)




