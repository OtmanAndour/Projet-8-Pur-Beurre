from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def redirection(request):
    return redirect('index')