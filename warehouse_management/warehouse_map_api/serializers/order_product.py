from django.urls import path, include
from warehouse_map_api.models.order_product import order_product  
from warehouse_map_api.models.product import Product
from warehouse_map_api.models.order import order as order_model
# from warehouse_map_api.serializers.product import ProductSerializer
# from warehouse_map_api.serializers.bill import BillSerializer
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=order_model.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    qty = serializers.DecimalField(decimal_places=14, max_digits=1000)
    class Meta:
        model = bill_product
        fields = ['order_id', 'product', 'qty', 'id']

    def create(self, validated_data):
        return order_product.objects.create(**validated_data)