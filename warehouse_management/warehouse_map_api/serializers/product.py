from django.db import models
from rest_framework import serializers
from warehouse_map_api.models.product import  Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    name = models.CharField(max_length=50)
    buy_price = models.DecimalField(decimal_places=14, max_digits=1000)
    sell_price = models.DecimalField(decimal_places=14, max_digits=1000)

    class Meta:
        model = Product
        fields = ['id', 'name', 'buy_price', 'sell_price']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.buy_price = validated_data.get('buy_price',instance.buy_price)
        instance.sell_price = validated_data.get('sell_price',instance)
        instance.save()
        return instance
