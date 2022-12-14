from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('scraper.api.urls')),
    path('auth/', include('rest_framework.urls')),
]
