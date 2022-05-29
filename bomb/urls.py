from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('food',views.food,name = 'food'),
    path('travel',views.travel,name = 'travel'),
    path('cars',views.cars,name = 'cars'),
]