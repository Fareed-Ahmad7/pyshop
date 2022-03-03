from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, default='hi')
    price = models.FloatField(default='1')
    stock = models.CharField(max_length=255, default='7')
    image_link = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=50, default='VCA2142')
    description = models.CharField(max_length=100, default='20% off on all products')
    discount = models.FloatField(default='0.2')
