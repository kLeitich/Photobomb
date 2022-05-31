from django.conf import settings
from django.urls import path,re_path
from django.conf.urls.static import static
from . import views

urlpatterns=[
    re_path('',views.welcome,name = 'welcome'),
    re_path('food',views.food,name = 'food'),
    re_path('travel',views.travel,name = 'travel'),
    re_path('cars',views.cars,name = 'cars'),
    re_path(r'^search/$',views.search_by_category,name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)