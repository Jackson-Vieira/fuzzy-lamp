from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('scraper.api.urls')),
    path('auth/', include('rest_framework.urls')),

    path('', views.index, name='index'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)