from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField("create published")


class ProductDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)