# from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from baskets.models import Basket
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'Authorisation',
               'form': form
               }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались. Добро пожаловать!')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {'title': 'Registration', 'form': form}
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    global total_quantity, total_sum, baskets
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=user)
        # Первый способ самый простой
        # total_quantity = 0
        # total_sum = 0
        # for basket in baskets:
            # total_quantity += basket.quantity
            # total_sum += basket.sum()

        # Второй способ _1
        # baskets = Basket.objects.filter(user=user)
        # total_quantity = sum(basket.quantity for basket in baskets)
        # total_sum = sum(basket.sum() for basket in baskets)
    context = {'title': 'Profile Users',
               'form': form,
               'baskets': Basket.objects.filter(user=user),
               # 'total_quantity': sum(basket.quantity for basket in baskets),# Способ 2 полный
               # 'total_sum': sum(basket.sum() for basket in baskets),

               }
    return render(request, 'users/profile.html', context)
