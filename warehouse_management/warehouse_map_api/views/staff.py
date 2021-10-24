# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from warehouse_map_api.services.staff import create_staff, get_staff, delete_staff, update_staff
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def add_staff(request):
    if request.method == 'POST':
        staff = create_staff(request.data)
        return Response(staff)

@api_view(['GET', 'DELETE', 'PUT'])
def staff_view(request, id):
    if request.method == 'GET':
        staff = get_staff(id)
        return Response(staff, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        delete_status = delete_staff(id)
        if delete_status == True:
            return Response("successfully deleted staff", status=status.HTTP_200_OK)
        elif delete_status == False:
            return Response("failed to delete staff", status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        staff = update_staff(request.data,id)
        return Response(staff, status=status.HTTP_200_OK)