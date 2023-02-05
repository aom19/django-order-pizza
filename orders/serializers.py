from .models import Order
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    flavour = serializers.CharField(max_length=40)
    quantity = serializers.IntegerField()
    order_status = serializers.HiddenField(default='P')
    class Meta:
        model = Order
        fields = ['id','size', 'flavour', 'quantity', 'order_status']

class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    flavour = serializers.CharField(max_length=40)
    quantity = serializers.IntegerField()
    order_status = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ['id','size', 'flavour', 'quantity', 'order_status', 'created_at', 'updated_at']


class OrderStatusUpadateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(max_length=20)
    class Meta:
        model = Order
        fields = ['order_status']