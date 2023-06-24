from django.contrib import admin
from django.urls import include, path
from .views import home, salvar

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
]
