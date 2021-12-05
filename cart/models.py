from django.db import models

# Create your models here.

class Cart(models.Model):
  user = models.OneToOneField( 'accounts.User', related_name="user_cart", on_delete=models.CASCADE)
  total = models.DecimalField( max_digits=10, decimal_places=2, default=0, blank=True, null=True)
  
  def __str__(self):
    return user + "'s Cart"

class CartItem(models.Model):
  cart = models.ForeignKey('Cart', related_name="cart_item", on_delete=models.CASCADE)
  product = models.ForeignKey('products.Product', related_name="cart_product", on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return product