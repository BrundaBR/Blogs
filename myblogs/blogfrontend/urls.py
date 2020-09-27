from django.contrib import admin
from django.urls import path,include
from blogfrontend import views
from django.conf.urls.static import static
from django.conf import settings
from blogbackend import views as vw

urlpatterns = [
    path('',vw.homepage,name='homepage'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
 