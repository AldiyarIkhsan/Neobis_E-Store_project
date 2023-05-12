from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        sum_price = 0
        products = validated_data.pop('products')
        validated_data.pop('summ')
        for p in products:
            sum_price += p.price
        instance = Order.objects.create(summ=sum_price, **validated_data)
        instance.products.set(products)
        return instance