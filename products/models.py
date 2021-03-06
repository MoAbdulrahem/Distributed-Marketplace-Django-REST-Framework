from django.db import models

# Create your models here.

class Review(models.Model):
  author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  review_body = models.CharField(max_length=3000)
  product = models.ForeignKey('products.Product', related_name='reviews', on_delete=models.CASCADE)
  
  REQUIRED_FIELDS = ['author', 'review_body', 'title', 'product']

  def __str__(self):
    return self.title


class Product(models.Model):
  name = models.CharField(max_length=200)
  short_description = models.CharField(max_length=300)
  long_description = models.CharField(max_length=3000)
  available = models.BooleanField(default=False)
  rating = models.FloatField(default=0)
  price = models.IntegerField()
  image = models.ImageField(null=True, blank=True ,default='empty.jpg', upload_to='media')
  # image = models.CharField(max_length=100000,default=None)
  amount = models.PositiveIntegerField(default=0)

  # Relationships
  seller = models.ForeignKey('accounts.User', related_name='products', on_delete=models.CASCADE)
  category = models.ForeignKey('categories.Category', related_name='categories', on_delete=models.CASCADE)

  REQUIRED_FIELDS = ['name', 'price', 'seller', 'category','image']

  def __str__(self):
    return self.name

class SoldProducts(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  image = models.ImageField(null=True, blank=True ,default='empty.jpg')
  quantity = models.PositiveIntegerField(default=0)

  # Relationships
  user = models.ForeignKey('accounts.User', related_name='sold_products', on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class PurchasedProducts(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  image = models.ImageField(null=True, blank=True ,default='empty.jpg')
  quantity = models.PositiveIntegerField(default=0)

  # Relationships
  user = models.ForeignKey('accounts.User', related_name='purchased_products', on_delete=models.CASCADE)

  def __str__(self):
    return self.name