# coding=utf-8

from django.shortcuts import render



def index(request):

    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')


def produtos_lista(request):
    return render(request, 'produtos_lista.html')


def produto(request):
    return render(request, 'produto.html')
