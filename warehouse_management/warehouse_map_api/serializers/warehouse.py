from django.urls import path, include
from warehouse_map_api.models.warehouse import warehouse 
from warehouse_map_api.models.location import location
from warehouse_map_api.serializers.location import LocationSerializer
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    brand_name = serializers.CharField()
    location = LocationSerializer()
    class Meta:
        model = warehouse
        fields = ['brand_name', 'location']
    
    def create(self, validated_data):
        print (validated_data)
        x = validated_data.get('location').get('geo_location_x')
        y = validated_data.get('location').get('geo_location_y')
        location_to_save = list(location.objects.filter(geo_location_x=x, geo_location_y=y))
        validated_data['location'] = location.objects.get(id=location_to_save[0].id)
        return warehouse.objects.create(**validated_data)
