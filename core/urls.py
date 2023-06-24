from django.urls import include, path
from .views import home, salvar, editar, delete, pesquisar

urlpatterns = [
    path('', home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('delete/<int:id>', delete, name='delete'),
    path('pesquisar/', pesquisar, name='pesquisar'),
]
