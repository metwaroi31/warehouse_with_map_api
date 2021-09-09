from django.urls import path, include
from warehouse_map_api.models.warehouse import warehouse 
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.Serializers):
    brand_name = serializers
    class Meta:
        model = warehouse
        fields = ['brand_name', 'location']
