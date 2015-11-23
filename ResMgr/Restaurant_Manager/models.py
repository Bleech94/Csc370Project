from django.db import models

# Create your models here.
class Restaurant(models.Model):
    phone_number = models.CharField(max_length = 16)
    address = models.CharField(primary_key = True, max_length = 40)
    postal_code = models.CharField(max_length = 7)

class Table(models.Model):
    number = models.IntegerField(primary_key = True)
    occupied = models.BooleanField()

class Order(models.Model):
    number = models.IntegerField(primary_key = True)

class FoodItem(models.Model):
    name = models.CharField(primary_key = True, max_length = 30)
    customer_price = models.FloatField()
    ingredient_price = models.FloatField()

class Menu(models.Model):
    menu_type = models.CharField(primary_key = True, max_length = 20)
