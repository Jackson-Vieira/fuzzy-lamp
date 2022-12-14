from django.shortcuts import render
from django.db.models.aggregates import Avg, Max, Min

from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from ..models import Link, Price
from .serializers import LinkSerializer

@api_view(['GET'])
def stats_view(request, id):
    stats = Link.objects.filter(pk=id).values('prices__price').aggregate(
        avg_price=Avg('prices__price'),
        min_price=Min('prices__price'),
        max_price=Max('prices__price')
    )
    return Response(stats)

class Links(ListAPIView):
    queryset = Link.objects.all() 
    serializer_class = LinkSerializer

class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def retrieve(self, request, *args, **kwargs):
        link = self.get_object()
        serializer = self.get_serializer(link)

        data = serializer.data
        stats = Link.objects.filter(pk=link.pk).values('prices__price').aggregate(
        avg_price=Avg('prices__price'),
        min_price=Min('prices__price'),
        max_price=Max('prices__price')
        )
        data['stats'] = stats
        return Response(data)

    def create(self, request, *args, **kwargs):
        user = request.user
        if not (Link.objects.filter(user=user).count() > 5):
            return super().create(request, *args, **kwargs)
        return Response('limit of links exceeded maximum allowed is 5.', status=status.HTTP_400_BAD_REQUEST)