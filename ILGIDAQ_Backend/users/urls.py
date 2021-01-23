from django.conf.urls import url, include
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LoginAPIView,RegisterView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),# 토큰 두가지 발행
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),# access토큰 재발행
    path('registration', RegisterView.as_view(), name="register"), #유저 등록
    path('login', LoginAPIView.as_view(), name="login"), # 로그인/인증 및 토큰 발행

]

