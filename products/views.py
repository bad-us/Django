import json
import os.path

from django.shortcuts import render
from products.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    context = {
        'title': 'Main Page',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Products',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    # file_path = os.path.join(MODULE_DIR, 'fixtures/products.json')
    # context['products'] = json.load(open(file_path, encoding='UTF-8'))
    return render(request, 'products/products.html', context)


