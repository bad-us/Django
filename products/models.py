from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description=models.TextField(blank=True)

class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images')
    description = models.CharField(max_length=1024, blank=True,null=True)
    short_description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
