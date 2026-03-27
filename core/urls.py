from django.contrib import admin
from django.urls import path
from leads import views
from django.urls import path, include   

urlpatterns = [
    path('', views.home, name='home'),  
    path('', include('leads.urls')),
    path('<slug:slug>/', views.page),
]