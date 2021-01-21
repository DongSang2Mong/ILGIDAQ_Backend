from django.urls import path
from .views import RegisterView, LoginAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path('registration', RegisterView.as_view(), name='registration'), #가입
    path('login', LoginAPIView.as_view(), name='login'), #로그인 인증
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
