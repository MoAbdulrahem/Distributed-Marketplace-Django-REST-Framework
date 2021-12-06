from rest_framework import serializers
from .models import Review, Product

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = ['author', 'review_body', 'title', 'product']


class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ['name', 'short_description', 'long_description', 'available', 'rating', 'price', 'seller', 'category','image']
