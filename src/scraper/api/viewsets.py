from django.db.models.aggregates import Avg, Max, Min

from django_filters import rest_framework as filters

from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView

from django.shortcuts import get_object_or_404

from ..models import Link
from .serializers import LinkSerializer
from .filters import LinkFilterSet
# @api_view(['GET'])
# @permission_classes([IsAuthenticated,])
# def myLinks(request):
#     links = Link.objects.filter(user=request.user)
#     serializer = LinkSerializer(links, many=True)
#     return Response(serializer.data)

class Links(ListAPIView):
    queryset = Link.objects.all() 
    serializer_class = LinkSerializer

class LinkViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.RetrieveModelMixin,
        GenericViewSet
        ):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LinkFilterSet

    def retrieve(self, request, *args, **kwargs, ):
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
        link = request.data.get('link')
        if not Link.objects.filter(link=link).exists():
            return super().create(request, *args, **kwargs)
        return Response({'message':'This link alrealdy exists'}, status=status.HTTP_400_BAD_REQUEST)

    # destroy