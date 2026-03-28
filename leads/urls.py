from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('submit/', views.submit),
    path('<slug:slug>/', views.page),
    path('ping/', views.ping),
]