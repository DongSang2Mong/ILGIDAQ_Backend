from rest_framework import routers
from django.conf.urls import url, include

from diary import views

diaryRouter = routers.DefaultRouter()
diaryRouter.register(r'diary', views.DiaryMetaViewset)
diaryRouter.register(r'diaryImage', views.DiaryImageViewset)

urlpatterns = [

    url(r'^', include(diaryRouter.urls)),

]