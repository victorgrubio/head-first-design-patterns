"""Main pizza execution script"""
from pizza import Pizza

def order_pizza(pizza_type: str) -> Pizza:
    pizza: Pizza = None
    if pizza_type == "cheese":
        pizza = CheesePizza()
    elif pizza_type == "greek":
        pizza = GreekPizza
    elif pizza_type == "pepperoni":
        pizza = PepperoniPizza()
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza