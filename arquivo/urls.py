from django.urls import path

from arquivo.views import home

urlpatterns = [
    path("", home),
]
