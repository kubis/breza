from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home_view(request):
    apps = AppType.objects.all()
    context = {
        'appartmets': apps,
    }
    return render(request, 'appartments/home.html', context)

def appartments_view(request):
    apps = AppType.objects.all()
    context = {
        'appartmets': apps,
    }
    return render(request, 'appartments/appartments.html', context)
