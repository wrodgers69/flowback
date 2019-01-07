from django.urls import include, path
from django.contrib import admin
from . import views
from flowback.views import home, success, well_information, well_data, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.index, name='index'),
    path('home/', home.as_view(), name='home'),
    path('success/', success.as_view(), name = 'success'),
    path('well_information/', well_information.as_view(), name = 'well_information'),
    path('well_data/', well_data.as_view(), name = 'inputdata'),
    path('logout/', logout.as_view(), name='logout'),
]
