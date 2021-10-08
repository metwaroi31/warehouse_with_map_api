from django.http import HttpResponse
from rest_framework.decorators import api_view
from warehouse_map_api.services.user import create_user, get_user, delete_user, update_user
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        user = create_user(request.data)
        return Response(user)

@api_view(['GET', 'DELETE', 'PUT'])
def user_view(request, id):
    if request.method == 'GET':
        user = get_user(id)
        return Response(user, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        delete_status = delete_user(id)
        if delete_status == True:
            return Response("successfully deleted user", status=status.HTTP_200_OK)
        elif delete_status == False:
            return Response("failed to delete user", status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        user = update_user(request.data,id)
        return Response(user, status=status.HTTP_200_OK)