# coding=utf-8

from django.shortcuts import render

from catalog.models import Category


def index(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')


