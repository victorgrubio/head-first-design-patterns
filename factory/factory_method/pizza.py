"""Abstract Pizza Class Module"""
import abc
from typing import List


class Pizza(abc.ABC):
    """Abstract Pizza Class"""
    # Pizzas have four main attributes: name, dough, sauce and toppings
    name: str
    dough: str
    sauce: str
    toppings: List[str] = []

    @classmethod
    def prepare(cls):
        """Prepares a pizza"""
        print(f'Preparing {cls.name}')
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings: ')
        for topping in cls.toppings:
            print(f'  {topping}')

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

    @classmethod
    def get_name(cls):
        """Gets the name of the pizza"""
        return cls.name
