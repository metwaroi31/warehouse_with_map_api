from django.db import models
from rest_framework import routers, serializers, viewsets
from warehouse_map_api.models.position import position
from warehouse_map_api.models.staff import staff

class StaffSerializer(serializers.HyperlinkedModelSerializer):
    name = models.CharField(max_length=50)
    position = models.ForeignKey(position, related_name='position', on_delete=models.CASCADE)
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
