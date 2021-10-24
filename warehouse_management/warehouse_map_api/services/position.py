from rest_framework.serializers import Serializer
from warehouse_map_api.serializers.position import PositionSerializer
from warehouse_map_api.models.position import position

def create_position(data):
    serializer = PositionSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
    return serializer.data

def get_position(pos_id):
    position_to_get = position.objects.get(id=pos_id)
    serializer = PositionSerializer(position_to_get)

    return serializer.data

def delete_position(pos_id):
    position_to_delete = position.objects.get(id=pos_id)
    position_to_delete.delete()
    
    return True

def update_position(data,pos_id):
    position_to_update = position.objects.get(id=pos_id)
    serializer = PositionSerializer(position_to_update,data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data