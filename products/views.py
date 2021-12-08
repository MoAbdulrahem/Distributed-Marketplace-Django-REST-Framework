from rest_framework import viewsets
from rest_framework import generics, status
from .models import Review, Product
from .serializers import ProductSerializer, ReviewSerializer
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
# from rest_framework.response import Response
from records.models import Record

# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  @action(detail=False, methods=['post'])
  @permission_classes((permissions.IsAuthenticated, ))
  def add_product(self, request):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      print(request.name+" x"+request.amount+ ", has been added by "+request.seller.email)
      Record.objects.create(report=request.name+" x"+request.amount+ ", has been added by "+request.seller.email)
      return Response(serializer.data)
    return Response({'status':'Failed'})

  @action(detail=False, methods=['post'])
  def showProductSeller(self, request):
    items = Product.objects.filter(seller=request.data['seller'])

    try:
      serializer = ProductSerializer(items, many=True)
      return Response(serializer.data)
    except:
      return Response(status.Http404)

  @action(detail=False, methods=['post'])
  def showProductCategory(self, request):
    items = Product.objects.filter(category=request.data['category'])

    try:
      serializer = ProductSerializer(items, many=True)
      return Response(serializer.data)
    except:
      return Response(status.Http404)
