from rest_framework import serializers
from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
  # products = serializers.PrimaryKeyRelatedField(many=True, queryset = Products.objects.all())
  password = serializers.CharField(max_length=64, min_length=6, write_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password']

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

    def create(self, validated_data):
      '''
      Responsible for creating the actual users
      '''
      return User.objects.create_user(**validated_data)
