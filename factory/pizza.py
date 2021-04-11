"""Abstract Pizza Class Module"""
import abc
from ingredients import Dough, Sauce, Veggies, Cheese, Pepperoni, Clams
from typing import List


class Pizza(abc.ABC):
    """Abstract Pizza Class"""
    # Pizzas had four main attributes: name, dough, sauce and toppings
    # Now they have custom ingredients    
    dough: Dough
    sauce: Sauce
    veggies: List[Veggies]
    cheese: Cheese
    pepperoni: Pepperoni
    clam: Clams

    def __init__(self):
        self.__name:str = ""

    @abc.abstractclassmethod
    def prepare(cls):
        """Abstract method to prepare a pizza
        
        This method is now abstract as each pizza would be prepared differently
        based on its ingredients.
        """     

    @classmethod
    def bake(cls):
        """Prepares a pizza"""
        print('Bake for 25 minutes at 350')

    @classmethod
    def cut(cls):
        """Cuts pizza in different pieces"""
        print('Cutting the pizza into diagonal slices')

    @classmethod
    def box(cls):
        """Put a pizza in a box"""
        print('Place pizza in official PizzaStore box')

    def get_name(self) -> str:
        """Gets the name of the pizza

        Returns:
            str: Name of pizza
        """
        return self.__name

    def set_name(self, name:str):
        """Sets name of pizza

        Args:
            name (str): New name for pizza
        """
        self.__name = name

    def __str__(self) -> str:
        """Overwritten print method

        Returns:
            str: Pizza as a string for printing
        """
        return self.__name