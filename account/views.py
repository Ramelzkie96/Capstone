from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_bits(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_Bits:
                    login(request, user)
                    return redirect('bits')
                else:
                    msg = 'Faculty account cant login'
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'

    return render(request, 'login_bits.html', {'form': form, 'msg': msg})




def login_faculty(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_Faculty:
                    login(request, user)
                    return redirect('faculty')
                else:
                    msg = 'Bits account cant login'
            else:
                msg = 'Ivalid creditial'
        else:
            msg = 'Error validating form'

    return render(request, 'login_faculty.html', {'form': form, 'msg': msg})

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='home')  # Change 'index' to 'login_bits' or the appropriate URL
def bits(request):
    return render(request, 'bits.html')

@login_required(login_url='home')  # Change 'index' to 'login_faculty' or the appropriate URL
def faculty(request):
    return render(request, 'faculty.html')


def bits_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_Bits:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')  # Redirect to the appropriate login page

    return _wrapped_view

def faculty_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_Faculty:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')  # Redirect to the appropriate login page

    return _wrapped_view


def home(request):
    return render(request, 'index.html')



