from rest_framework.serializers import Serializer
from warehouse_map_api.serializers.order import OrderSerializer
from warehouse_map_api.services.map_api import get_directions

def create_order(data):
    serializer = OrderSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
    
    data
    
    return serializer.data