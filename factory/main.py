"""Factory method main module"""

from pizza import Pizza
from pizza_store import PizzaStore
from ny.pizza_store import NYPizzaStore


if __name__ == "__main__":
    ny_store: PizzaStore = NYPizzaStore()
    pizza: Pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.get_name()}")