from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("", views.index, name="index"),
    path("customer/<int:user_id>/place-an-order", views.place_an_order, name="place_an_order"),
    path("customer/<int:user_id>/add/<int:order_id>", views.add, name="add"),
    path("customer/<int:user_id>/cart/<int:order_id>", views.cart, name="cart"),
    path("customer/<int:user_id>/checkout/<int:order_id>", views.checkout, name="checkout"),
    path("customer/<int:user_id>/view-orders", views.view_orders, name="view_orders"),
    path("emp", views.emp_index, name="emp_index"),
    path("employee/view-orders", views.emp_view_orders, name="emp_view_orders"),
    path("employee/update/<int:order_id>", views.emp_update_order, name="emp_update_order"),
]