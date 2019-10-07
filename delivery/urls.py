from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from delivery import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(r"delivery/", views.Create_Delivery.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
    path('reached_pickup/', views.reached_pickup,name='reached_pickup'),
    path('delivery_completed/', views.delivery_completed,name='delivery_completed'),
    path('get_location/', views.get_location,name='get_location'),
]

