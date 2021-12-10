from rest_framework import serializers
from .models import Cart, CartItem
from accounts.serializers import RegisterSerializer 
from products.serializers import ProductSerializer 
from products.models import Product


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ["cart",
        "product" ,
        "quantity",
        ]


class CartSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Cart
    #     fields = ("user", 'total')
    user = RegisterSerializer(read_only=True)
    cart_item = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # products = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = (
            'id', 
            'user', 
            'cart_item', 
        )
        depth = 2


