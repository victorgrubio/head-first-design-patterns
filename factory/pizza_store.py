"""Abstract Pizza Store Class"""
import abc
from pizza import Pizza


class PizzaStore(abc.ABC):
    """Abstract class for Pizza Store
    It contains the implementation of Factory Method at create_pizza

    This method will be overwritten by subclass to share the same behaviour
    """

    @classmethod
    def order_pizza(cls, pizza_type: str) -> Pizza:
        """Orders a pizza of a concrete type

        Args:
            pizza_type (str): Type of pizza to create

        Returns:
            Pizza: Pizza ordered, cut in a box
        """
        pizza: Pizza = None
        pizza = cls.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


    @abc.abstractclassmethod
    def create_pizza(cls, pizza_type: str) -> Pizza:
        """Creates a pizza based on its type. Abstract method with Factory Method functionality.

        Args:
            pizza_type (str): Type of pizza to create

        Returns:
            Pizza: Pizza created
        """
        pass