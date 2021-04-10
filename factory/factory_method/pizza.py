"""Module containing all pizza types"""
import abc
from typing import List


class Pizza(abc.ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str] = []

    @abc.abstractclassmethod
    def prepare(cls):
        print(f'Preparing {cls.name}')
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings: ')
        for topping in cls.toppings:
            print(f'  {topping}')

    @abc.abstractclassmethod
    def bake(cls):
        print('Bake for 25 minutes at 350')

    @abc.abstractclassmethod
    def cut(cls):
        print('Cutting the pizza into diagonal slices')
    
    @abc.abstractclassmethod
    def box(cls):
        print('Place pizza in official PizzaStore box')
    
    @abc.abstractclassmethod
    def get_name(cls):
        return cls.name
