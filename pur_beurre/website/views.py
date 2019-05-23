from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from datetime import datetime

User = get_user_model()

# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def redirection(request):
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html', {'form': form})

@login_required
def account(request):
    return render(request, 'website/account.html')