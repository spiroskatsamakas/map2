# Create your views here.
# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def map(request):
    return render(request, 'map.html')