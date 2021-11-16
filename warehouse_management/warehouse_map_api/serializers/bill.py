from django.urls import path, include
from warehouse_map_api.models.bill import bill
from warehouse_map_api.models.bill_product import bill_product
from warehouse_map_api.serializers.bill_product import BillProductSerializer
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class BillSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    received_date = serializers.CharField(max_length=1000)
    price = serializers.DecimalField(decimal_places=14, max_digits=1000)
    bill_products = BillProductSerializer(many=True, required=False)

    class Meta:
        model = bill
        fields = ['price', 'received_date', 'id', 'bill_products']

    def create(self, validated_data):
        # price = validated_data.get('price')
        # received_date = validated_data.get('received_date')

        bill_price = validated_data.pop('price', None)
        bill_received_date = validated_data.pop('received_date', None)
        bill_products = validated_data.pop('bill_products', None)
        bill_to_add =  bill.objects.create(price=bill_price, received_date=bill_received_date)

        for bill_product_item in bill_products:
            quantity = bill_product_item.get('qty')
            product = bill_product_item.get('product')
            bill_product.objects.create(qty=quantity, product=product, bill=bill_to_add)
        
        return bill_to_add

    def update(self, instance, validated_data):
        price = validated_data.get('price')
        received_date = validated_data.get('received_date')
        
        instance.price = price
        instance.received_date = received_date
        instance.save()
        return instance
