from django.shortcuts import render
from django.http import HttpResponse

from bomb.models import Image

# Create your views here.
def welcome(request):
    images=Image.objects.all()
    return render(request, 'index.html',{'images':images})

def food(request):
    return render(request, 'food.html')

def travel(request):
    return render(request, 'travel.html')

def cars(request):
    return render(request, 'cars.html')


