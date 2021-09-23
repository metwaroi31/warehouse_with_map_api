from rest_framework.serializers import Serializer
from warehouse_map_api.serializers.staff import StaffSerializer

def create_staff(data):
    serializer = StaffSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
    return serializer.data