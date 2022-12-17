from django.urls import path
from rest_framework.routers import SimpleRouter

from . import viewsets

app_name = 'scraper'

urlpatterns = [
    # path('me/links/', viewsets.myLinks, name='me_links')
]

router = SimpleRouter()
router.register('links', viewsets.LinkViewSet)
urlpatterns += router.urls