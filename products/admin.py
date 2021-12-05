from django.contrib import admin
from .models import Review, Product
# Register your models here.

admin.site.register(Product)
admin.site.register(Review)