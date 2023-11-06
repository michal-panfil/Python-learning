from datetime import datetime
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, default="No name")
    category = models.CharField(max_length=200, default="General")



class ProductDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='details')
    description = models.CharField(max_length=200, default="No description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    sku = models.CharField(max_length=200, default="000000")
    create_date = models.DateTimeField(default=datetime.now, blank=True)