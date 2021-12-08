from django.db import models

# Create your models here.

class Record(models.Model):
  title = models.CharField(max_length=200, default = "Transaction")
  report = models.CharField(max_length=2000)

  def __str__(self):
    return self.title