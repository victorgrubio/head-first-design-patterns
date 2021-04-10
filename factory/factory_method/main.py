"""Factory method main module"""

from factory_method.pizza import Pizza
from factory_method.pizza_store import PizzaStore
from factory_method.ny import NYPizzaStore


if __name__ == "__main__":
    ny_store: PizzaStore = NYPizzaStore()
    pizza: Pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.get_name()}")