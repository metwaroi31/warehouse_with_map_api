from django.http import HttpResponse
from rest_framework.decorators import api_view
from warehouse_map_api.services.product import *
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        product = create_product(request.data)
        return Response(product)

@api_view(['GET', 'DELETE', 'PUT'])
def product_view(request, id):
    if request.method == 'GET':
        product = get_product(id)
        return Response(product, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        delete_status = delete_product(id)
        if delete_status == True:
            return Response("successfully deleted product", status=status.HTTP_200_OK)
        elif delete_status == False:
            return Response("failed to delete product", status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        product = update_product(request.data,id)
        return Response(product, status=status.HTTP_200_OK)