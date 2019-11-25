from django.conf.urls import url
from rest_framework import routers
from .views import UserInfoCreate, UserInfoDetail, UserInfoUpdate, UserInfoDelete

urlpatterns = [
    url(r'^signup/$', UserInfoCreate.as_view()),
    url(r'^mypage/$', UserInfoDetail.as_view()),
    url(r'^update/$', UserInfoUpdate.as_view()),
    url(r'^delete/$', UserInfoDelete.as_view()),
]