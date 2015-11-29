from django.db import models

# Create your models here. migrations folder tracks all changes
class Receipt(models.Model):
	number = models.AutoField(primary_key = True)
	table = models.IntegerField(default = -1)
	customer_total = models.FloatField(null = True)
	ingredient_total =  models.FloatField(null = True)
	date = models.DateTimeField(auto_now = True)
	def get_profit(self):
		return round((self.customer_total - self.ingredient_total), 2)
	profit = property(get_profit)

class Order(models.Model):
	number = models.AutoField(primary_key = True)
	customer = models.IntegerField(default = -1)
	foodItem = models.CharField(max_length = 30)

class FoodItem(models.Model):
    name = models.CharField(primary_key = True, max_length = 30)
    customer_price = models.FloatField()
    ingredient_price = models.FloatField()
