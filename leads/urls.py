from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('submit/', views.submit),
    path('success/', views.success),  # thêm dòng này    
    path('limit/', views.limit),
    path('ping/', views.ping),
    path('<slug:slug>/', views.page),
]