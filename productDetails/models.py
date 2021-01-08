# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Category(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Manufacturer(models.Model):
    Name = models.CharField(max_length = 100)
    AddressLine1 = models.CharField(max_length = 100)
    AddressLine2 = models.CharField(max_length = 100)
    PinCode = models.IntegerField()
    def __str__(self):
        return self.Name

# Create your models here.
class productDetails(models.Model):
    product_Name = models.CharField(max_length = 100)
    category_Id = models.ForeignKey(Category, on_delete= models.CASCADE)
    manufacturer_Id = models.ForeignKey(Manufacturer, on_delete= models.CASCADE)
    rack_No = models.IntegerField()
    price = models.IntegerField()

class productPath(models.Model):
    rack = models.IntegerField()
