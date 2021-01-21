from django.conf.urls import url, include
from rest_framework import routers

from users import views

##이거도

userRouter = routers.DefaultRouter()
userRouter.register(r'user-login', views.UserLoginInfoViewset)

urlpatterns = [

    url(r'^', include(userRouter.urls)),
###
    url(r'^user-profile$', views.UserProfileView.as_view()),
  
]