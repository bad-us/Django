import json
import os.path

from django.shortcuts import render
from products.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    context = {
        'title': 'Main Page',
    }
    return render(request, 'products/index.html', context)


# def products(request):
#     context = {
#         'title': 'Products',
#         'products': Product.objects.all(),
#         'categories': ProductCategory.objects.all(),
#     }
#     # file_path = os.path.join(MODULE_DIR, 'fixtures/products.json')
#     # context['products'] = json.load(open(file_path, encoding='UTF-8'))
#     return render(request, 'products/products.html', context)

# def products(request, category_id=None):
#     context = {'title': 'Products', 'categories': ProductCategory.objects.all()}
#     if category_id:
#         context['products'] = Product.objects.filter(category_id=category_id)
#     else:
#         context['products'] = Product.objects.all()
#     return render(request, 'products/products.html', context)

def products(request, category_id=None, page=1):
    context = {'title': 'Products', 'categories': ProductCategory.objects.all()}
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)
