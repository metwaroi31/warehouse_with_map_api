from django.http import HttpResponse
from rest_framework.decorators import api_view
from warehouse_map_api.services.order import *
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def add_order(request):
    if request.method == 'POST':
        order = create_order(request.data)
        return Response(order, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_order_list_view(request, index):
    if request.method == 'GET':
        order_list = get_order_list(index)
        return Response(order_list, status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE', 'PUT'])
def order_view(request, id):
    if request.method == 'GET':
        order = get_order(id)
        return Response(order, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        delete_status = delete_order(id)
        if delete_status == True:
            return Response("successfully deleted order", status=status.HTTP_200_OK)
        elif delete_status == False:
            return Response("failed to delete order", status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        order = update_order(request.data,id)
        return Response(order, status=status.HTTP_200_OK)