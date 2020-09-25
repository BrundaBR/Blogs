from django.contrib import admin
from django.urls import path,include

from blogbackend import views


urlpatterns = [
    path('',views.backend,name="app"),
    ]
