from rest_framework import serializers
from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
  # products = serializers.PrimaryKeyRelatedField(many=True, queryset = Products.objects.all())
  password = serializers.CharField(max_length=64, min_length=6, write_only=True)
  user_cart = serializers.PrimaryKeyRelatedField(read_only=True)
  products = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
  sold_products = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
  purchased_products = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
  class Meta:
    model = User
    fields = ['id' ,'username', 'email', 'password', 'balance', 'products', 'user_cart', 'purchased_products', 'sold_products']
    write_only_fields = ('password')
    read_only_fields = ('is_staff', 'is_superuser')
    # depth = 2

  def validate(self, attrs):
    '''
    Gets called whenever we user .is_valid() in views, performs validation of the request.data
    '''
    email = attrs.get('email', '')
    username = attrs.get('username', '')

    if not username:
      raise serializers.ValidationError('Username must be provided.')

    if not email:
      raise serializers.ValidationError('Email must be provided.')
    
    return attrs

    # def create(self, validated_data):
    #   '''
    #   Responsible for creating the actual users
    #   '''
    #   return User.objects.create_user(**validated_data)

  def create(self, validated_data):
    '''
    test version
    '''
    password = validated_data.pop('password')
    user = super().create(validated_data)
    user.set_password(password)
    # Cart.objects.create(user=self.user)
    user.save()
    return user
    
