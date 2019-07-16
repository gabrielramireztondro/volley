from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    count = User.objects.count()
    if User.is_authenticated:
        page="home.html"
    else:
        page="login/login.html"
    return render(request, page, {'Usuarios': count})
