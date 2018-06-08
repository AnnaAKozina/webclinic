from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<patient_id>[0-9]+)/$', views.detail, name='detail'),
]
