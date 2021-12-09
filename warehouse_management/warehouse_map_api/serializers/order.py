from django.core.exceptions import ImproperlyConfigured
from django.db.models.query import QuerySet
from django.urls import path, include
from rest_framework.relations import PrimaryKeyRelatedField
from warehouse_map_api.serializers.warehouse import WarehouseSerializer
from warehouse_map_api.models.order import order 
from warehouse_map_api.serializers.location import LocationSerializer
from warehouse_map_api.models.warehouse import warehouse 
from warehouse_map_api.models.staff import staff 
from warehouse_map_api.models.location import location
from rest_framework import routers, serializers, viewsets
from warehouse_map_api.models.order_product import order_product
from warehouse_map_api.models.product import Product

# Serializers define the API representation.
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    staff = PrimaryKeyRelatedField(queryset=staff.objects.all(), many=False)
    warehouse= PrimaryKeyRelatedField(queryset=warehouse.objects.all(), many=False)
    directions = serializers.CharField(max_length=1000)
    moneynumber=serializers.IntegerField()
    location = LocationSerializer()
    order_details_to_add = serializers.ListField(child=serializers.JSONField(), required=False)

    class Meta:
        model = order
        fields = ['id','staff','warehouse', 'directions', 'location','moneynumber', 'order_details_to_add']
    
    def create(self, validated_data):
        x = validated_data.get('location').get('geo_location_x')
        y = validated_data.get('location').get('geo_location_y')
        location_to_save = list(location.objects.filter(geo_location_x=x, geo_location_y=y))
        validated_data['location'] = location.objects.get(id=location_to_save[0].id)
        order_details = validated_data.pop('order_details_to_add')
        order_to_add = order.objects.create(**validated_data)

        for order_item in order_details:
            quantity = order_item.get('qty')
            product = order_item.get('product')
            product_detail = Product.objects.get(pk=product)
            order_product.objects.create(qty=quantity, product=product_detail, order=order_to_add.id)

        return order_to_add

    def update(self, instance, validated_data):
        instance.staff = validated_data.get('staff',instance.staff)
        instance.directions = validated_data.get('directions',instance.directions)
        instance.location = validated_data.get('location',instance.location)
        instance.warehouse = validated_data.get('warehouse',instance.warhouse)
        instance.moneynumber = validated_data.get('moneynumber',instance.moneynumber)
        instance.save()
        return instance
