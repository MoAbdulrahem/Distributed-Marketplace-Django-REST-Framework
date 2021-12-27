from django.contrib import admin
from .models import PurchasedProducts, Review, Product, SoldProducts
# Register your models here.

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(SoldProducts)
admin.site.register(PurchasedProducts)