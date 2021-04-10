"""Module containing all pizza types"""
import abc
from typing import List


class Pizza(abc.ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str] = []

    @classmethod
    def prepare(cls):
        print(f'Preparing {cls.name}')
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings: ')
        for topping in cls.toppings:
            print(f'  {topping}')

    @classmethod
    def bake(cls):
        print('Bake for 25 minutes at 350')

    @classmethod
    def cut(cls):
        print('Cutting the pizza into diagonal slices')

    @classmethod
    def box(cls):
        print('Place pizza in official PizzaStore box')

    @classmethod
    def get_name(cls):
        return cls.name
