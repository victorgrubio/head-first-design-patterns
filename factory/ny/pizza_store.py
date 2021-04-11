"""Pizza stores for NY Area module"""
from pizzas import CheesePizza, VeggiePizza, ClamPizza, PepperoniPizza
from ny.pizza_ingredient_factory import NYPizzaIngredientFactory
from pizza_ingredient_factory import PizzaIngredientFactory
from pizza_store import PizzaStore
from pizza import Pizza


class NYPizzaStore(PizzaStore):
    """Pizza store for NY Area

    Previously implements the abstract class Pizza Store as a Factory for create_pizza factory method.
    Now it implements an Abstract Factory for Pizza creation based on ingredients
    """

    @classmethod
    def create_pizza(cls, pizza_type: str) -> Pizza:
        """Creates a pizza. Factory method subclass implementation

        Args:
            pizza_type (str): Type of pizza to create

        Returns:
            Pizza: Created pizza
        """
        pizza: Pizza = None
        ingredient_factory: PizzaIngredientFactory = NYPizzaIngredientFactory()
        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")
        if pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")
        if pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")
        if pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")
        return pizza