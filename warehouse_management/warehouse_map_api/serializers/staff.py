from django.db import models
from rest_framework import routers, serializers, viewsets
from warehouse_map_api.models.staff import staff

class StaffSerializer(serializers.HyperlinkedModelSerializer):
    name = models.CharField(max_length=50)
    # location = models.ForeignKey(location, related_name='location', on_delete=models.CASCADE)
    class Meta:
        model = staff
        fields = ['name']
    
    def create(self, validated_data):
        return staff.objects.create(**validated_data)
