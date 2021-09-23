from warehouse_map_api.models.warehouse import warehouse
from rest_framework.serializers import Serializer
from warehouse_map_api.serializers.warehouse import WarehouseSerializer
from warehouse_map_api.services.location import create_location 

def add_warehouse(data):
    location = data.pop('location')
    location_serializer = create_location(data=location)
    data['location'] = location_serializer
    serializer = WarehouseSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data