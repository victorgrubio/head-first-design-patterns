"""Abstract Pizza Store Class"""
import abc
from factory_method.pizza import Pizza


class PizzaStore(abc.ABC):
    """Abstract class for Pizza Store
    """
    @classmethod
    def order_pizza(cls, pizza_type: str) -> Pizza:
        pizza: Pizza = None
        pizza = cls.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


    @abc.abstractclassmethod
    def create_pizza(cls, pizza_type: str) -> Pizza:
        pass