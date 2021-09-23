from rest_framework.serializers import Serializer
from warehouse_map_api.serializers.location import LocationSerializer

def create_location(data):
    serializer = LocationSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
    return serializer.data