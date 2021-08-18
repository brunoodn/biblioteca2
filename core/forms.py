from django import forms
from .models import Autores, Editoras, Livros

class AutoresModelForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['nome']

class EditorasModelForm(forms.ModelForm):
    class Meta:
        model = Editoras
        fields = ['nome']

class LivrosModelForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['nome','autor', 'editora', 'preco']

