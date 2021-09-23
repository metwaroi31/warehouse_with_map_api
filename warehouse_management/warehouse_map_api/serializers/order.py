from django.urls import path, include
from warehouse_map_api.models.order import order 
from warehouse_map_api.serializers.location import LocationSerializer
from warehouse_map_api.serializers.staff import StaffSerializer
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    staff = StaffSerializer()
    directions = serializers.CharField(max_length=1000)
    location = LocationSerializer()
    class Meta:
        model = order
        fields = ['staff', 'directions', 'location']
    
    def create(self, validated_data):
        return order.objects.create(**validated_data)
