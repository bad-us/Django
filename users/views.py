from django.shortcuts import render

# Create your views here.
def login(request):
    context = {'title': 'Authorisation'
    }
    return render(request, 'users/login.html', context)

def register(request):
    context = {'title': 'Registration'
    }
    return render(request, 'users/register.html', context)