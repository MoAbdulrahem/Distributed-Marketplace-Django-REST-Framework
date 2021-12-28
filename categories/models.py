from django.db import models

# Create your models here.


class Category(models.Model):
  name = models.CharField(max_length=200, unique=True)
  # icon = models.ImageField(upload_to=None, height_field=50, width_field=50,)
  description = models.CharField(max_length=2000)

  verbose_name = 'Category'
  verbose_plural_name = 'Categories'
  
  def __str__(self):
    return self.name