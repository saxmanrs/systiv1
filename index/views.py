from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from home.views import home



# Create your views here.


@login_required
def index_urls(request):
    return render(request, 'index.html')


def my_logout(request):
    logout(request)
    return redirect('home')



@login_required
def cad_urls(request):
    return render (request,'cadastro.html')

