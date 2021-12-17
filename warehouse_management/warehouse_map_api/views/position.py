from django.http import HttpResponse
from rest_framework.decorators import api_view
from warehouse_map_api.services.position import *
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_position(request):
    if request.method == 'POST':
        position = create_position(request.data)
        return Response(position)

@api_view(['GET', 'DELETE', 'PUT'])
def position_view(request, id):
    if request.method == 'GET':
        position = get_position(id)
        return Response(get_position, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        delete_status = delete_position(id)
        if delete_status == True:
            return Response("successfully deleted position", status=status.HTTP_200_OK)
        elif delete_status == False:
            return Response("failed to delete position", status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        position = update_position(request.data,id)
        return Response(position, status=status.HTTP_200_OK)

@api_view(['GET'])
def position_list_view(request):
    if request.method == 'GET':
        position_list = get_all_position()
        response_data = {}
        response_data["list"] = position_list
        return Response(response_data, status=status.HTTP_200_OK)