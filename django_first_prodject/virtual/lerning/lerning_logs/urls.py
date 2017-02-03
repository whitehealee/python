"""Определяет схемы URL для learning_logs."""
from django.conf.urls import *

from . import views

urlpatterns = (
    url(r'^$', views.current_datetime, name='home'),
    url(r'^hello/$', views.hello, name='index'),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead, name='index'),
)
