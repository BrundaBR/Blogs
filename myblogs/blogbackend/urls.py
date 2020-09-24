from django.contrib import admin
from django.urls import path,include
from blogbackend import views

urlpatterns = [
    path('app/',views.backend,name="app"),
    
]
