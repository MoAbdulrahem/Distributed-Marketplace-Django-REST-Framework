from rest_framework import viewsets
from rest_framework import generics, status
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.response import Response

# Create your views here.

class CartViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer





class CartItemViewSet(viewsets.ModelViewSet):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer
  @action(detail=False, methods=['post'])
  def itemInTheCart(self, request):
      items = CartItem.objects.filter(quantity = int(request.data['quantity']))
     
      try:
          serializer = CartItemSerializer(items)
          return Response(serializer.data)
      except:
          return Response(status.Http404)
      return Response({'status':'cannot find'})



