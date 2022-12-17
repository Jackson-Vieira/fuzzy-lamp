from ..models import Link

from django_filters import rest_framework as filters


class LinkFilterSet(filters.FilterSet):
    
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Link
        fields = ('name',)