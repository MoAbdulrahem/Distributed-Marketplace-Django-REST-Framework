from rest_framework import viewsets
from rest_framework import generics, status
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.status import Http404
from accounts.serializers import RegisterSerializer
from accounts.models import User
from products.models import Product

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
      items = CartItem.objects.filter(cart = request.data['cart'])
     
      try:
          serializer = CartItemSerializer(items, many=True)
          return Response(serializer.data)
      except:
          return Response({'status':'failed'})
      return Response({'status':'cannot find'})


  @action(detail=False, methods=['post'])
  def checkout(self, request):
    
    cart_instance = Cart.objects.get(user=request.user) # Get the cart for the user that issued the request
    # cart = CartSerializer(cart_instance)
    # items = CartItem.objects.filter(cart = cart_instance)
    items = cart_instance.cart_item.all() # get all items associated with that car, by using reverse relation

    # TESTING: print the items instide the cart.
    total_cost = 0
    owners = {} #keep track of what each owner balance would be after their items are sold
    for item in items: #each item is a CartItem instance, so it has the product and its amount but NOT its price
      product_instance = Product.objects.get(pk=item.product.id)
      print(item.product, " Quantity: ", item.quantity, " ID: ", item.id, " price: ", product_instance.price)
      total_cost += (product_instance.price*item.quantity)
      owners[product_instance.seller]= product_instance.price*item.quantity
      print("total_cost: ", total_cost)
    # product_set = Product.objects.all()
    # products = product_set.cart_product.all()
    # for product in products:
    #   print("Product is ", product )

    #Getting the product price
    # products = 

    serializer=RegisterSerializer(request.user)

    if request.user.balance >= total_cost:
      return_dict = {'status':'Transaction Complete, Balance was deducted by: '+str(total_cost)}
      request.user.balance -= total_cost
      request.user.save()
      print("balance was deducted by ", total_cost)
      for key in owners:
        owner = User.objects.get(email=key)
        owner.balance += owners[key]
        owner.save()
        return_dict[owner.email] = 'Balance increased by: '+str(owners[key])
        print (key, "balance increased by:" , owners[key])

      return Response(return_dict)

    else:
      print("transaction failed, Balance is not enough.")
      return Response({'status':'Transaction Failed, Balance is not sufficient.'})

    return Response(serializer.data)




