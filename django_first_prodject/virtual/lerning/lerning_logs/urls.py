"""Определяет схемы URL для learning_logs."""
from django.conf.urls import *

from . import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
)