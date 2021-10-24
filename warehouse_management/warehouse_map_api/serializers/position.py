from warehouse_map_api.models.position import position
from django.db import models
from rest_framework import serializers


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    name = models.CharField(max_length=50)
    class Meta:
        model = position
        fields = ['id', 'name']

    def create(self, validated_data):
        return position.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance
