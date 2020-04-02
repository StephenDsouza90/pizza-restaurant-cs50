from django.contrib import admin
from .models import FoodCategory, RegularPizza, SicilianPizza, Topping, Sub, Pasta, Salad, DinnerPlatter, CustOrder, CustOrderSelection

admin.site.register(FoodCategory)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(CustOrder)
admin.site.register(CustOrderSelection)
