from rest_framework.serializers import ModelSerializer

from django.db.models.aggregates import Max, Min, Avg

from ..models import Link

class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('__all__')
        