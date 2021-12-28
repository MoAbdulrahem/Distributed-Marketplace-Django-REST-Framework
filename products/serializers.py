from rest_framework import serializers
from .models import PurchasedProducts, Review, Product, SoldProducts

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = ['author', 'review_body', 'title', 'product']


class ProductSerializer(serializers.ModelSerializer):
  # reviews = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
  reviews = serializers.SlugRelatedField(read_only=True,many=True, slug_field='title')
  class Meta:
    model = Product
    fields = [
      'id',
      'name',
      'short_description',
      'long_description',
      'available',
      'amount',
      'rating',
      'price',
      'seller',
      'category',
      'image',
      'reviews',
      ]
    # depth = 1

class SoldProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = SoldProducts
    fields = ['author', 'review_body', 'title', 'product']

class PurchasedSerializer(serializers.ModelSerializer):
  class Meta:
    model = PurchasedProducts
    fields = ['author', 'review_body', 'title', 'product']