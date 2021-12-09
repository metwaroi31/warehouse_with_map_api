# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from warehouse_map_api.services.warehouse import add_warehouse, get_warehouse, delete_warehouse, update_warehouse, \
                                                    get_warehouse_list
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_warehouse_view(request):
    if request.method == 'POST':
        warehouse = add_warehouse(request.data)
        return Response(warehouse, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_warehouse_list_view(request, index):
    if request.method == 'GET':
        list_of_warehouse = get_warehouse_list(index)
        return Response(list_of_warehouse, status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE', 'PUT'])
def warehouse_view(request, id):
    if request.method == 'GET':
        warehouse = get_warehouse(id)
        return Response(warehouse, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        delete_status = delete_warehouse(id)
        if delete_status == True:
            return Response("successfully deleted warehouse", status=status.HTTP_200_OK)
        elif delete_status == False:
            return Response("failed to delete warehouse", status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        warehouse = update_warehouse(request.data, id)
        return Response(warehouse, status=status.HTTP_200_OK)
