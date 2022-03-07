from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# http://127.0.0.1:8034

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')