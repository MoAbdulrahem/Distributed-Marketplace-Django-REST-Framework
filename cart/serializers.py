from rest_framework import serializers
from .models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("user", 'total')


class CartItemSerializer(serializers.ModelSerializer):
    # product = CartProductSerializer(required=False)
    class Meta:
        model = CartItem
        fields = ["cart", "product", "quantity"]
