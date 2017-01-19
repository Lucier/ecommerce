# coding=utf-8

from django.shortcuts import render

from .models import Product, Category

def produtos_lista(request):
    context = {
    'produtos_lista': Product.objects.all()
    }
    return render(request, 'catalog/produtos_lista.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),
    }
    return render(request, 'catalog/category.html', context)
