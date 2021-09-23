# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from warehouse_map_api.services.warehouse import add_warehouse
from rest_framework.response import Response
# from warehouse_map_api.serializers.warehouse import WarehouseSerializer

# @api_view(['PUT', 'GET', 'DELETE'])
# def warehouse (request):
#     if request.method == 'PUT' :
#         warehouse = add_warehouse(request.data)
#         return Response(warehouse)
    
#     if request.method == 'GET' :
#         warehouse

@api_view(['POST'])
def add_warehouse_view(request):
    if request.method == 'POST':
        warehouse = add_warehouse(request.data)
        return Response(warehouse)
