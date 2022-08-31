from order.models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    product = serializers.CharField(max_length=50)
    size = serializers.CharField(max_length=50,default='Small')
    order_status = serializers.HiddenField(default='Not_Delivered')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = [
            'product','size','order_status','quantity','created_at'
        ]


class OrderDetailsSerializer(serializers.ModelSerializer):
    product = serializers.CharField(max_length=50)
    size = serializers.CharField(max_length=50,default='Small')
    order_status = serializers.CharField(default='Not_Delivered')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = [
            'product','size','order_status','quantity','created_at','updated_at'
        ]

class OrderStatusUpdate(serializers.ModelSerializer):
    order_status = serializers.CharField(default='Not_Delivered')

    class Meta:
        model = Order
        fields = ['order_status']


class UserOderById(serializers.ModelSerializer):
    product = serializers.CharField(max_length=50)
    size = serializers.CharField(max_length=50,default='Small')
    order_status = serializers.CharField(default='Not_Delivered')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = [
            'product','size','order_status','quantity','created_at'
        ]
