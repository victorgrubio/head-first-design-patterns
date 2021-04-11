from pizza_ingredient_factory import PizzaIngredientFactory
from pizza import Pizza


class CheesePizza(Pizza):

    pizza_ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.pizza_ingredient_factory = ingredient_factory

    
    def prepare(self):
        print(f"Preparing {self}")
        self.dough = self.pizza_ingredient_factory.create_dough()
        self.sauce = self.pizza_ingredient_factory.create_sauce()
        self.cheese = self.pizza_ingredient_factory.create_cheese()