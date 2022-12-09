from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListAPIView

from ..models import Link, Price
from ..tasks import update_data_price

from .serializers import LinkSerializer

from time import time

@api_view(['GET'])
def update(request):
    links = Link.objects.all()
    for link in links:
        update_data_price.delay(link.id)
    response = {
        'message': f'estimated time to finish {links.count()*2}s',
    }
    return Response(response, status=status.HTTP_200_OK)


class Links(ListAPIView):
    queryset = Link.objects.all() 
    serializer_class = LinkSerializer
