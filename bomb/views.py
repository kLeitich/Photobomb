from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def pic_food(request):
    return render(request, 'food.html')

def pic_food(request):
    return render(request, 'travel.html')

def pic_food(request):
    return render(request, 'food.html')

def pic_food(request):
    return render(request, 'food.html')
