from rest_framework.serializers import Serializer
from warehouse_map_api.models.order import order
from warehouse_map_api.serializers.order import OrderSerializer
from warehouse_map_api.services.map_api import get_directions
from warehouse_map_api.services.location import *
def create_order(data):
    serializer = OrderSerializer(data=data)
    location = data.pop('location')
    location_serializer = create_location(data=location)
    data['location'] = location_serializer
    if serializer.is_valid():
        serializer.save() 
    return serializer.data

def get_order(order_id):
    order_to_get = order.objects.get(id=order_id)
    serializer = OrderSerializer(order_to_get)

    return serializer.data

def delete_order(order_id):
    order_to_delete= order.objects.get(id=order_id)
    order_to_delete.delete()
    return True

def update_order(data,order_id):
    order_to_update = order.objects.get(id=order_id)
    serializer = OrderSerializer(order_to_update,data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data