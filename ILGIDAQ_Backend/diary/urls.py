from django.conf.urls import url, include
from rest_framework import routers

from diary import views

diaryRouter = routers.DefaultRouter()
diaryRouter.register(r'diary', views.DiaryMetaViewset)



urlpatterns = [

    url(r'^', include(diaryRouter.urls)),
    url(r'^diaryImage/$', views.DiaryImageList.as_view()),
    url(r'^diaryImage/(?P<pk>.+/[0-9]+)/$', views.DiaryImageDetail.as_view()),
    url(r'^diaryContent/$', views.DiaryContentList.as_view()),
    url(r'diaryContent/(?P<pk>.+)/$', views.DiaryContentDetail.as_view()),

]

