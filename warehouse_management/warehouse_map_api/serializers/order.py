from django.urls import path, include
from warehouse_management.warehouse_map_api.serializers.warehouse import WarehouseSerializer
from warehouse_map_api.models.order import order 
from warehouse_map_api.serializers.location import LocationSerializer
from warehouse_map_api.serializers.staff import StaffSerializer
from warehouse_map_api.models.warehouse import warehouse 
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    staff = StaffSerializer()
    warehouse= WarehouseSerializer()
    directions = serializers.CharField(max_length=1000)
    moneynumber=serializers.IntegerField()
    location = LocationSerializer()
    class Meta:
        model = order
        fields = ['id','staff','warehouse', 'directions', 'location','moneynumber']
    
    def create(self, validated_data):
        return order.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.staff = validated_data.get('staff',instance.staff)
        instance.directions = validated_data.get('directions',instance.directions)
        instance.location = validated_data.get('location',instance.location)
        instance.warehouse = validated_data.get('warehouse',instance.warhouse)
        instance.moneynumber = validated_data.get('moneynumber',instance.moneynumber)
        instance.save()
        return instance
