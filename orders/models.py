from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class FoodCategory(models.Model):
    """ Represents food categories """

    category_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category_name}"


class RegularPizza(models.Model):
    """ Represents Regular Pizza """

    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"


class SicilianPizza(models.Model):
    """ Represents Sicilian Pizza """

    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"


class Topping(models.Model):
    """ Represents Pizza Topping """

    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Sub(models.Model):
    """ Represents Sub """

    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"


class Pasta(models.Model):
    """ Represents Pasta """

    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Salad(models.Model):
    """ Represents Salad """

    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class DinnerPlatter(models.Model):
    """ Represents Dinner Platter """

    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"


class CustOrder(models.Model):
    """ Customer orders """

    cust_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    order_status = models.CharField(max_length=64, null=True, blank=True)
    bill_amount = models.DecimalField(max_digits=999, decimal_places=2, null=True, blank=True)
    checkout_time = models.DateTimeField(null=True, blank=True) 

    class Meta:
        verbose_name_plural = "Customer order"


class CustOrderSelection(models.Model):
    """ Items customer has ordered """

    order_id = models.ForeignKey(CustOrder, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=64)
    category = models.CharField(max_length=64, null=True, blank=True)
    food_size = models.CharField(max_length=64, null=True, blank=True)
    food_price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField()
    total_per_item = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name_plural = "Customer Order Selection"


class Customer:
    """ Handle customer methods """

    def view_menu(self):
        regular_pizza = RegularPizza.objects.all()
        sicilian_pizza = SicilianPizza.objects.all()
        toppings = Topping.objects.all()
        subs = Sub.objects.all()
        pastas = Pasta.objects.all()
        salads = Salad.objects.all()
        dinner_platter = DinnerPlatter.objects.all()
        return regular_pizza, sicilian_pizza, toppings, subs, pastas, salads, dinner_platter

    def create_order_id(self, user_id):
        order_id = CustOrder(cust_id_id=user_id)
        order_id.save()
        return order_id

    def add_food_to_order(self, order_id, food_name, category, food_size, food_price, quantity, total_per_item):
        add = CustOrderSelection(order_id_id=order_id, food_name=food_name, category=category, food_size=food_size,
                food_price=food_price, quantity=quantity, total_per_item=total_per_item)
        add.save()
        return add

    def view_cart(self, user_id, order_id):
        items = CustOrderSelection.objects.filter(order_id_id=order_id)
        return items

    def checkout(self, user_id, order_id, order_status, checkout_time, bill_amount):
        checkout = CustOrder.objects.filter(id=order_id).update(
            order_status=order_status,
            checkout_time=checkout_time,
            bill_amount=bill_amount
            )
        return checkout

    def view_orders(self, user_id):
        orders = CustOrder.objects.filter(cust_id=user_id)
        return orders
        

class Employee:
    """ Handle employee methods """

    def view_orders(self):
        orders = CustOrder.objects.all()
        return orders

    def update_order(self, order_id, order_status):
        update = CustOrder.objects.filter(id=order_id).update(order_status=order_status)
        return update


def get_grand_total(order_id):
    """ Customer can view the grand total of an order """

    result = CustOrderSelection.objects.filter(order_id_id=order_id)
    total = []
    for i in result:
        total.append(i.total_per_item)
    bill_amount = sum(total)
    return bill_amount