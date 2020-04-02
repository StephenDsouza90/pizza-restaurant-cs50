import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import Customer, Employee, get_grand_total


def signup(request):
    """ Customer signup """

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if not first_name or not last_name or not username or not email or not password:
            context = {"message": "Please enter all credentials"}
            return render(request, "error.html", context)
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.info(request, 'Signup successful!')
            return redirect("login")
    else:
        return render(request, "signup.html") 


def user_login(request):
    """ Customer/Employee login """

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if not username or not password:
            context = {"message": "Please enter all credentials"}
            return render(request, "error.html", context)
        else:
            user = authenticate(request, username=username, password=password)
            superuser = User.objects.filter(is_superuser=True)
            for name in superuser:
                # Check if Employee
                if name.username == username:
                    login(request, user)
                    return redirect("emp_index")
                # Check if Customer
                else:
                    login(request, user)
                    return redirect("index")
    else:
        return render(request, "login.html")


def user_logout(request):
    """ User logout """

    logout(request)
    return render(request, "login.html")


### Customer functions
def index(request):
    """ Users can see menu """

    if request.user.is_authenticated:
        regular_pizza, sicilian_pizza, toppings, subs, pastas, salads, dinner_platter = Customer.view_menu(request)
        context = {
            "regular_pizza": regular_pizza,
            "sicilian_pizza": sicilian_pizza,
            "toppings": toppings,
            "subs": subs,
            "pastas": pastas,
            "salads": salads,
            "dinner_platter": dinner_platter
            }
        return render(request, "index.html", context) 
    else:
        return render(request, "login.html")
        

def place_an_order(request, user_id):
    """ Users can place an order """

    if request.user.is_authenticated:
        order_id = Customer.create_order_id(request, user_id)
        context = {
            "order_id": order_id
            }
        return render(request, "place_order.html", context)
    else:
        return render(request, "login.html")


def add(request, user_id, order_id):
    """ Add items to cart """

    if request.user.is_authenticated:
        regular_pizza, sicilian_pizza, toppings, subs, pastas, salads, dinner_platter = Customer.view_menu(request)
        context = {
            "order_id": order_id,
            "regular_pizza": regular_pizza,
            "sicilian_pizza": sicilian_pizza,
            "toppings": toppings,
            "subs": subs,
            "pastas": pastas,
            "salads": salads,
            "dinner_platter": dinner_platter
            }
        if request.method == "POST":
            order_id = order_id
            food_name = request.POST.get('food_name', '')
            category = request.POST.get("category", '')
            food_size = request.POST.get("food_size", '')
            food_price = request.POST.get("food_price", 0)
            quantity = request.POST.get("quantity", '')
            total_per_item = float(food_price) * int(quantity)
            Customer.add_food_to_order(request, order_id, food_name, 
                category, food_size, food_price, quantity, 
                "%.2f" % total_per_item)
            messages.info(request, 'Add successful!')
        return render(request, "menu_selection.html", context)


def cart(request, user_id, order_id):
    """ Views cart before checking out """

    if request.user.is_authenticated:
        items = Customer.view_cart(request, user_id, order_id)
        bill_amount = get_grand_total(order_id)
        context = {
            "order_id": order_id,
            "items": items,
            "grand_total": bill_amount
            }
        return render(request, "cart.html", context)
    else:
        return render(request, "login.html")


def checkout(request, user_id, order_id):
    """ Checkout confirmed """

    if request.user.is_authenticated:
        order_status = "Order confirmed"
        checkout_time = datetime.datetime.now()
        bill_amount = get_grand_total(order_id)
        Customer.checkout(request, user_id, order_id, order_status, checkout_time, bill_amount)
        context = {
            "order_id": order_id
            }
        messages.info(request, 'Checkout successful!')
        return render(request, "checkout.html", context)
    else:
        return render(request, "login.html")


def view_orders(request, user_id):
    """ Customer can view their orders """

    if request.user.is_authenticated:
        orders = Customer.view_orders(request, user_id)
        context = {
            "orders": orders
            }
        return render(request, "orders.html", context)
    else:
        return render(request, "login.html")


### Employee functions
def emp_index(request):
    """ Employee Home Page """

    if request.user.is_authenticated:
        return render(request, "employee/index.html")


def emp_view_orders(request):
    """ Employee can view all orders """

    if request.user.is_authenticated:
        orders = Employee.view_orders(request)
        context = {
            "orders": orders
            }
        return render(request, "employee/orders.html", context)
    else:
        return render(request, "login.html")


def emp_update_order(request, order_id):
    """ Employee can update an order status """

    if request.user.is_authenticated:
        order_status = "Order Completed"
        Employee.update_order(request, order_id, order_status)
        messages.info(request, 'Update successful!')
        return render(request, "employee/update.html")
    else:
        return render(request, "login.html")