"""Pizza Store that implements the Simple Factory"""
from simple_factory.simple_pizza_factory import SimplePizzaFactory
from simple_factory.pizza import Pizza


class PizzaStore(object):
    pizza_factory: SimplePizzaFactory = None

    def __init__(self, pizza_factory: SimplePizzaFactory):
        self.factory = pizza_factory

    @classmethod
    def order_pizza(cls, pizza_type: str) -> Pizza:
        pizza :Pizza = None
        pizza = cls.pizza_factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza