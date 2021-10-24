from rest_framework.serializers import Serializer
from warehouse_map_api.serializers.staff import StaffSerializer
from warehouse_map_api.models.staff import staff

def create_staff(data):
    serializer = StaffSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
    return serializer.data

def get_staff(staff_id):
    staff_to_get = staff.objects.get(id=staff_id)
    serializer = StaffSerializer(staff_to_get)

    return serializer.data

def delete_staff(staff_id):
    staff_to_delete = staff.objects.get(id=staff_id)
    staff_to_delete.delete()
    
    return True

def update_staff(data,staff_id):
    staff_to_update = staff.objects.get(id=staff_id)
    serializer = StaffSerializer(staff_to_update,data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data