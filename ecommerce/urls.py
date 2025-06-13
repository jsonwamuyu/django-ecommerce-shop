from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('shop.urls', namespace="shop")),  # Uncomment if you have a shop app
]