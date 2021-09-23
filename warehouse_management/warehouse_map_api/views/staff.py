# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from warehouse_map_api.services.staff import create_staff
from rest_framework.response import Response
# from warehouse_map_api.serializers.warehouse import WarehouseSerializer


@api_view(['POST'])
def add_staff(request):
    if request.method == 'POST':
        staff = create_staff(request.data)
        return Response(staff)