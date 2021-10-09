from rest_framework.serializers import Serializer
from warehouse_map_api.serializers.user import UserSerializer
from warehouse_map_api.models.user import user

def create_user(data):
    serializer = UserSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
    return serializer.data

def get_user(user_id):
    user_to_get = user.objects.get(id=user_id)
    serializer = UserSerializer(user_to_get)

    return serializer.data

def delete_user(user_id):
    user_to_delete = user.objects.get(id=user_id)
    user_to_delete.delete()
    
    return True

def update_user(data,user_id):
    user_to_update = user.objects.get(id=user_id)
    serializer = UserSerializer(user_to_update,data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data