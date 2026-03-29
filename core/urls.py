from django.contrib import admin
from django.urls import path
from leads import views
from django.urls import path, include   

urlpatterns = [
    path('', include('leads.urls')),
]