from django.urls import path
from .views import index, autores, editoras, livros

urlpatterns = [
    path('', index,name='index'),
    path('autores', autores, name='autores'),
    path('editoras', editoras,name='editoras'),
    path('livros', livros, name='livros'),


]

