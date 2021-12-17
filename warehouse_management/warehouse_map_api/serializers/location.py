from django.urls import path, include
from warehouse_map_api.models.location import location 
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    geo_location_x = serializers.CharField(max_length=1000)
    geo_location_y = serializers.CharField(max_length=1000)
    class Meta:
        model = location
        fields = ['geo_location_x', 'geo_location_y']

    def create(self, validated_data):
        # print (validated_data)
        x = validated_data.get('geo_location_x')
        y = validated_data.get('geo_location_y')
        existing_location = list(location.objects.filter(geo_location_x=x, geo_location_y=y))
        print (existing_location)
        if len(existing_location) != 0:
            return existing_location[0]
        return location.objects.create(**validated_data)