from django.urls import path

from . import views

app_name = 'scraper'

urlpatterns = [
    path('links/', views.Links.as_view(), name='links'),
    path('update/', views.update, name='update')
]