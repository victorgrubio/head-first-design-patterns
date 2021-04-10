"""Abstract Pizza Store Class"""
from abc import ABC, abstractmethod
from factory_method.pizza import Pizza


class PizzaStore(ABC):
    """Abstract class for Pizza Store
    """
    
    def order_pizza(pizza_type: str) -> Pizza:
        pizza: Pizza = None
        pizza = create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


    @abstractmethod
    def create_pizza(pizza_type: str) -> Pizza:
        pass