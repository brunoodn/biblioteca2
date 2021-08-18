from django.shortcuts import render
from core.forms import AutoresModelForm, EditorasModelForm, LivrosModelForm
from django.contrib import messages
from .models import Autores, Editoras, Livros
# Create your views here.

def index(request):
    return render(request, 'index.html')


def autores(request):
    if str(request.method) == 'POST':
        form = AutoresModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor criado com sucesso..')
            form = AutoresModelForm()
        else:
            messages.error(request, 'erro ao salvar..')

    else:
        form = AutoresModelForm()
    context = {
        'autores': Autores.objects.all(),
        'form': form
    }

    return render(request, 'autores.html', context)


def editoras(request):
    if str(request.method) == 'POST':
        form = EditorasModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salvo com sucesso..')
            form = EditorasModelForm()
        else:
            messages.error(request, 'Erro ao salvar..')
    else:
        form = EditorasModelForm()
    context = {
        'editoras': Editoras.objects.all(),
        'form': form
    }
    return render(request, 'editoras.html', context)


def livros(request):
    if str(request.method) == 'POST':
        form = LivrosModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salvo com sucesso.')
            form = LivrosModelForm()
        else:
            messages.error(request, 'Erro ao salvar.')
    else:
        form = LivrosModelForm()
    context = {
        'livros': Livros.objects.all(),
        'form': form
    }
    return render(request, 'livros.html', context)
