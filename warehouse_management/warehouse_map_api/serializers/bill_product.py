from django.urls import path, include
from warehouse_map_api.models.bill_product import bill_product  
from warehouse_map_api.models.product import Product
# from warehouse_map_api.serializers.product import ProductSerializer
# from warehouse_map_api.serializers.bill import BillSerializer
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class BillProductSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    bill = serializers.PrimaryKeyRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    qty = serializers.DecimalField(decimal_places=14, max_digits=1000)
    class Meta:
        model = bill_product
        fields = ['bill', 'product', 'qty', 'id']

    def create(self, validated_data):
        return bill_product.objects.create(**validated_data)