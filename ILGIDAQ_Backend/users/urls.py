from django.conf.urls import url, include
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LoginAPIView, ProfileUpdateAPI, ProfileListAPI, ProfileDetailAPI
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),# 토큰 두가지 발행
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),# access토큰 재발행
    path('login', LoginAPIView.as_view(), name="login"), # 로그인/인증 및 토큰 발행 (계정 미존재시 계정발급)
    path('<int:user_pk>/profile', ProfileUpdateAPI.as_view(), name='profile-list'), #프로필들 업데이트
    path('profile/list', ProfileListAPI.as_view()), #프로필 리스트 조회
    path('<int:user_pk>/profile/detail', ProfileDetailAPI.as_view())#하나의 프로필 정보 조회 및 수정

]

