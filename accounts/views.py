from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, status
from .models import User
from accounts.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth import authenticate, login
# Create your views here.
# TODO: Handle user log in.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @action(detail=False, methods=['post'])
    def loginCheck(self, request):
        users = list(self.get_queryset())
        for user in users:
        
            if user.email==request.data['email'] and user.password == request.data['password']:
                try:
                    serializer = RegisterSerializer(user )
                    return Response(serializer.data)
                except:
                    return Response(status.Http404)
        return Response({'status':'not a user'})

    # @action(detail=False, methods=['post'])
    # def loginCheck(self, request):
    #     account = authenticate(request, email=request.data['email'], password=request.data['password'])
    #     print(account)
    #     if account is not None:
    #       login(request, account)
    #       user = User.objects.get(email=request.data['email'])
    #       serializer = RegisterSerializer(user)
    #       return Response(serializer.data)
    #     else:
    #       return Response({'status':'FAILED'})
