from django.urls import path
from rest_framework.routers import SimpleRouter

from . import viewsets

app_name = 'scraper'

urlpatterns = [
    # path('links/', viewsets.Links.as_view(), name='links'),
    path('stats/<int:id>/', viewsets.stats_view, name='stats')
]


router = SimpleRouter()
router.register('links', viewsets.LinkViewSet)
urlpatterns += router.urls