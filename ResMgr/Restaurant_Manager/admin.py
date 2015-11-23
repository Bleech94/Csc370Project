from django.contrib import admin

# Register your models here.
from .models import Restaurant
from .models import Table
from .models import Order
from .models import FoodItem
from .models import Menu

admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(FoodItem)
admin.site.register(Menu)
