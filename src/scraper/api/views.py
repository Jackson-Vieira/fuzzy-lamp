from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Link, Price
from ..tasks import update_data_price

from time import time

@api_view(['GET'])
def update(request):
    links = Link.objects.all()
    for link in links:
        update_data_price.delay(link.id)
    message = {}
    return Response('OK!')

