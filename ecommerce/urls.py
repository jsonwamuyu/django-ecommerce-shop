
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

# from .sites import new_admin as new_admin  # Import the custom Unfold admin site


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('unfold-admin/', new_admin),  # Include Unfold admin URLs
     path('', include('shop.urls', namespace="shop")),  # Uncomment if you have a shop app

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)