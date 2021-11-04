from django.http import HttpResponse
from rest_framework.decorators import api_view
from warehouse_map_api.services.bill import *
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_bill(request):
    if request.method == 'POST':
        bill = create_bill(request.data)
        return Response(bill, status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def bill_view(request, id):
    if request.method == 'GET':
        bill = get_bill(id)
        return Response(bill, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        delete_status = delete_bill(id)
        if delete_status == True:
            return Response("successfully deleted position", status=status.HTTP_200_OK)
        elif delete_status == False:
            return Response("failed to delete position", status=status.HTTP_404_NOT_FOUND)

