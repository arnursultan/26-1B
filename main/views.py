from django.shortcuts import render
from django.http import JsonResponse
import django

def home_view(request):
    return render(request, 'main/home.html')

def about(request):
    ctx = {
        "framework": "Django",
        "version": django.get_version(),
    }
    return render(request, 'main/about.html', ctx)

def echo(request):
    data = {
        "method": request.method,
        "params": request.GET,
    }
    return JsonResponse(data)