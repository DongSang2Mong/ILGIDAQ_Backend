from django.conf.urls import url, include
from rest_framework import routers

from diary import views

# ([0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})


diaryRouter = routers.DefaultRouter()
diaryRouter.register(r'diary', views.DiaryMetaViewset)



urlpatterns = [

    url(r'^', include(diaryRouter.urls)),

    url(r'^diary-image/$', views.DiaryImageList.as_view()),
    url(r'^diary-image/(?P<dk>([0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}))/$', views.DiaryImageWithKey.as_view()),
    url(r'^diary-image/(?P<pk>([0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})/[0-9]+)/$', views.DiaryImageDetail.as_view()),

    url(r'^diary-content/$', views.DiaryContentList.as_view()),
    url(r'^diary-content/(?P<pk>([0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}))/$', views.DiaryContentDetail.as_view()),

]

