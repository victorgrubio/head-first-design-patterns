"""Module that contains all NY Pizza Types"""
from pizza import Pizza


class NYStyleCheesePizza(Pizza):
    name = "NY Style Sauce and Cheese Pizza"
    dough = "Thin Crust Dough"
    sauce = "Marinara Sauce"
    toppings = ["Grated Reggiano Cheese"]


class NYStyleVeggiePizza(Pizza):
    pass


class NYStyleClamPizza(Pizza):
    pass


class NYStylePepperoniPizza(Pizza):
    pass