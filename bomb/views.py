from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def food(request):
    return render(request, 'food.html')

def travel(request):
    return render(request, 'travel.html')

def cars(request):
    return render(request, 'cars.html')


