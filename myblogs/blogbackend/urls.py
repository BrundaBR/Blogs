from django.contrib import admin
from django.urls import path,include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    
)
from blogbackend import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.backend,name="app"),
    path('post/<pk>/', PostDetailView.as_view(), name='detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    ]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
