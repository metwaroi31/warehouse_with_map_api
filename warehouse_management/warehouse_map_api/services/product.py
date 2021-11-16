from rest_framework.serializers import Serializer
from warehouse_map_api.serializers.product import ProductSerializer
from warehouse_map_api.models.product import Product

def create_product(data):
    serializer = ProductSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
    return serializer.data

def get_product(product_id):
    product_to_get = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product_to_get)

    return serializer.data

def delete_product(product_id):
    product_to_delete = Product.objects.get(id=product_id)
    product_to_delete.delete()
    
    return True

def update_product(data,product_id):
    product_to_update = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product_to_update,data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data