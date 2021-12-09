from rest_framework.serializers import Serializer
from warehouse_map_api.models.order import order
from warehouse_map_api.serializers.order import OrderSerializer
from warehouse_map_api.services.map_api import get_directions
from warehouse_map_api.services.location import *
from warehouse_map_api.models.order_product import order_product
from warehouse_map_api.serializers.product import ProductSerializer
def create_order(data):
    serializer = OrderSerializer(data=data)
    location = data.pop('location')
    location_serializer = create_location(data=location)
    data['location'] = location_serializer
    if serializer.is_valid():
        serializer.save() 
    detail_order = get_detail_order(serializer.data["id"])
    return_order = serializer.data
    return_order["products"] = detail_order
    return return_order

def get_order_list(index):
    orders = order.objects.all()
    start_index = index * 10 - 10
    end_index = index * 10
    serializer = OrderSerializer(orders[start_index:end_index], many=True)
    return serializer.data

def get_order(order_id):
    order_to_get = order.objects.get(id=order_id)
    serializer = OrderSerializer(order_to_get)
    detail_order = get_detail_order(order_id)
    return_order = serializer.data
    return_order["order_detail"] = detail_order
    return return_order

def delete_order(order_id):
    order_to_delete= order.objects.get(id=order_id)
    order_to_delete.delete()
    return True

def update_order(data,order_id):
    order_to_update = order.objects.get(id=order_id)
    serializer = OrderSerializer(order_to_update,data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data

def get_detail_order(order_id):
    return_detail_bill = []
    order_products_to_get = order_product.objects.filter(order=order_id)
    raw_order_products = list(order_products_to_get)
    
    for order_detail in raw_order_products:
        # get product serializer
        custom_JSON = {}
        custom_JSON["product"] = order_detail.product.__dict__
        custom_JSON
        serializer = ProductSerializer(order_detail.product)
        return_detail_bill.append(serializer.data)
    return return_detail_bill 
