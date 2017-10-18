from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.get_details , name='get_details'),
    url(r'^success$', views.mailsend , name='mailsend'),
]