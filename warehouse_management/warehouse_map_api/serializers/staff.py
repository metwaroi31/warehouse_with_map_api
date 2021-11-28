from django.db import models
from rest_framework import routers, serializers, viewsets
from warehouse_map_api.models.staff import staff
from warehouse_map_api.models.position import position
class StaffSerializer(serializers.HyperlinkedModelSerializer):
    name = models.CharField(max_length=50)
    position = serializers.PrimaryKeyRelatedField(queryset=position.objects.all() ,many=False)
    # change to integer field
    
    class Meta:
        model = staff
        fields = ['id','name','position']
    
    def create(self, validated_data):
        return staff.objects.create(**validated_data)
 
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.position = validated_data.get('position',instance.position)
        instance.save()
        return instance
