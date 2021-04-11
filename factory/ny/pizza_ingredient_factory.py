"""NY Ingredient Factory for Pizzas"""
from typing import List
from pizza_ingredient_factory import PizzaIngredientFactory
from ny.ingredients import (
    ThinCrustDough, MarinaraSauce, ReggianoCheese, Garlic, Onion,  Mushroom, RedPepper, SlicedPepperoni, FreshClams
)
from ingredients import Veggies


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    @classmethod
    def create_dough(cls) -> ThinCrustDough:
        return ThinCrustDough()

    @classmethod
    def create_sauce(cls) -> MarinaraSauce:
        return MarinaraSauce()

    @classmethod
    def create_cheese(cls) -> ReggianoCheese:
        return ReggianoCheese()
    
    @classmethod
    def create_veggies(cls) -> List[Veggies]:
        veggies: List[Veggies] = [
            Garlic(), Onion(), Mushroom(), RedPepper()
        ]
        return veggies

    @classmethod
    def create_pepperoni(cls) -> SlicedPepperoni:
        return SlicedPepperoni()

    @classmethod
    def create_clam(cls) -> FreshClams:
        return FreshClams()