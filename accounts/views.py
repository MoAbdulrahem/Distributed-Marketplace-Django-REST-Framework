from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, status
from .models import User
from accounts.serializers import RegisterSerializer
from rest_framework.response import Response

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# class UserViewSet(viewsets.ViewSet):
#   """
#   A simple ViewSet for listing or retrieving users.
#   """
#   def list(self, request):
#       queryset = User.objects.all()
#       serializer = RegisterSerializer(queryset, many=True)
#       return Response(serializer.data)

#   def retrieve(self, request, pk=None):
#       queryset = User.objects.all()
#       user = get_object_or_404(queryset, pk=pk)
#       serializer = RegisterSerializer(user)
#       return Response(serializer.data)

# class RegisterView(generics.GenericAPIView):

#   serializer_class = RegisterSerializer

#   def post(self, request):
#     user = request.data
#     serializer = self.serializer_class(data=user)
#     if serializer.is_valid():
#       serializer.save()
    
#       user_data = serializer.data

#       return Response(user_data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
