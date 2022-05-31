from django.conf import settings
from django.urls import path,re_path
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('food',views.food,name = 'food'),
    path('travel',views.travel,name = 'travel'),
    path('cars',views.cars,name = 'cars'),
    path('search/',views.search_by_category,name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)