
from django.shortcuts import render
from django.http import HttpResponse

from bomb.models import Category, Image,Location

# Create your views here.
def welcome(request):
    images=Image.objects.all()
    return render(request, 'index.html',{'images':images})

def food(request,category):
    
    return render(request, 'food.html')

def travel(request):
    return render(request, 'travel.html')

def cars(request):
    return render(request, 'cars.html')

def search_by_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_cat = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"category": searched_cat})
    else:
        message = "You haven't searched for any category"
        return render(request,'search.html')
