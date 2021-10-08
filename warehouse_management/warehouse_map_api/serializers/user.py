from warehouse_map_api.models.user import user
from django.db import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        model = user
        fields = ['id', 'username', 'name', 'password']

    def create(self, validated_data):
        return user.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.password = validated_data.get('password',instance.password)
        instance.save()
        return instance
