"""Pizza stores for NY Area module"""
from factory_method.pizza_store import PizzaStore
from factory_method.pizza import Pizza
from factory_method.ny import NYStyleCheesePizza, NYStyleVeggiePizza, NYStyleClamPizza, NYStylePepperoniPizza


class NYPizzaStore(PizzaStore):
    """Pizza store for NY Area

    Implements the abstract class Pizza Store as a Factory for create_pizza factory method
    """

    @classmethod
    def create_pizza(cls, pizza_type: str) -> Pizza:
        """Creates a pizza. Factory method subclass implementation

        Args:
            pizza_type (str): Type of pizza to create

        Returns:
            Pizza: Created pizza
        """
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        if pizza_type == "veggie":
            return NYStyleVeggiePizza()
        if pizza_type == "clam":
            return NYStyleClamPizza()
        if pizza_type == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None