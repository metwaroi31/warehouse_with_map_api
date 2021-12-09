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

def get_warehouse(warehouse_id):
    warehouse_to_get = warehouse.objects.get(id=warehouse_id)
    serializer = WarehouseSerializer(warehouse_to_get)

    return serializer.data

def get_warehouse_list(index):
    warehouses = warehouse.objects.all()
    start_index = index * 10 - 10
    end_index = index * 10
    serializer = WarehouseSerializer(warehouses[start_index:end_index], many=True)
    return serializer.data

def delete_warehouse(warehouse_id):
    warehouse_to_delete = warehouse.objects.get(id=warehouse_id)
    warehouse_to_delete.delete()
    
    return True

def update_warehouse(data, warehouse_id):
    location = data.pop('location')
    location_serializer = create_location(data=location)
    data['location'] = location_serializer

    warehouse_to_update = warehouse.objects.get(id=warehouse_id)
    serializer = WarehouseSerializer(warehouse_to_update, data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data