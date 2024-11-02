from django.urls import path

from . import api

urlpatterns = [
    path('', api.file_list, name='file_list'),
]