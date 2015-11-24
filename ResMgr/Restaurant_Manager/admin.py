from django.contrib import admin

# Register your models here.

from .models import Receipt
from .models import Order
from .models import FoodItem

admin.site.register(Receipt)
admin.site.register(Order)
admin.site.register(FoodItem)

