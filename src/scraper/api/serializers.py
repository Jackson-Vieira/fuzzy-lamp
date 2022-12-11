from rest_framework.serializers import ModelSerializer

from django.db.models.aggregates import Max, Min, Avg

from ..models import Link

class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = (
            'id','name', 'link_type', 'image_url',
            'link', 'updated', 'created', 
            'situation', 'current_price', 
            'old_price', 'price_difference')
        read_only_fields = (
            'id','name', 'image_url', 'updated', 
            'created', 'situation', 'current_price', 
            'old_price', 'price_difference')
        # extra_kwargs { 'field': {'read_only':True}}