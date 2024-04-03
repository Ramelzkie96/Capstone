from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_Bits:
                login(request, user)
                return redirect('bits')
            elif user is not None and user.is_Faculty:
                login(request, user)
                return redirect('faculty')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def logoutUser(request):
    logout(request)
    return redirect('login_view')

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
            return redirect('login_view')  # Redirect to the appropriate login page

    return _wrapped_view

def faculty_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_Faculty:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login_view')  # Redirect to the appropriate login page

    return _wrapped_view



