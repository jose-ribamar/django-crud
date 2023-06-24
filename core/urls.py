from django.urls import include, path
from .views import home, pesquisar, salvar, editar, update, delete

urlpatterns = [
    path('', home, name='home'),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('pesquisar/', pesquisar, name='pesquisar'),
]
