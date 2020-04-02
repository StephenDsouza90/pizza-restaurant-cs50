# Project 3: Pizza 

In this web application, customers can sign up and login to view the menu of **Pizza Restaurant** and place online orders.

The categories are:

1. Regular Pizza
2. Sicilian Pizza
3. Toppings
4. Subs
5. Pasta
6. Salads
7. Dinner Platters

The customers can place orders by clicking **Place an order** and then add items to their cart by clicking **Add to cart**. Place an order will first generate an Order ID and then the customer can add as many items as they want to their cart. 

Customers can go back and forth between viewing their cart and adding more items to their cart by clicking **Go to cart** and **Want to add more items?** respectively. Once the customers have selected all the items they want, they can confirm their order by clicking **Confirm order**. 

Before the checkout, the customers have a view of all items in the cart and the total bill. The customers can also view their orders and see the status of their order.

There is also an Employee interface (Site administrator). The employee can view all orders that have been placed by customers and can update the status of an order.

## Models

The `models.py` layer is the database layer that has all the classes which creates tables in the DB. There is also an Employee class and Customer class along with its respective methods for interacting with the other classes (Classes which are used for creating tables in the DB).

## Views

The `views.py` layer is the business logic layer that interacts between the database layer and user interface layer. All the business logic are models in their respective functions.

## URLS

The `urls.py` has all the routes which are mapped to the respective functions in `views.py`.

## Superuser

The Superuser (in this case the Employee) has been created by using:

```

>> python manage.py createsuperuser

```

Items in the menu have been added to the DB by using the Django's Admin UI.

## Install Dependencies

The dependencies are saved in the requirements.txt file. 

It can be installed via the following command:

```

>> pip install -r requirements.txt

```

## How to run locally

```

>> python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 16, 2020 - 13:27:15
Django version 3.0.2, using settings 'pizza.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```