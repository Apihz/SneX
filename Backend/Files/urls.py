from django.urls import path

from . import api

urlpatterns = [
    path('/', api.file_list, name='file_list'),
    path('upload/', api.file_upload, name='file_upload'),
]