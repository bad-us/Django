from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title': 'Geekshop',
        'header': 'Hello people!',
        'username': 'Bad',
    }
    return render(request, 'products/test_context.html')