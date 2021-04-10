from factory_method.pizza_store import PizzaStore
from factory_method.pizza import Pizza
from factory_method.ny import NYStyleCheesePizza, NYStyleVeggiePizza, NYStyleClamPizza, NYStylePepperoniPizza


class NYPizzaStore(PizzaStore):

    @classmethod
    def create_pizza(cls, item: str) -> Pizza:
        if item == "cheese":
            return NYStyleCheesePizza()
        if item == "veggie":
            return NYStyleVeggiePizza()
        if item == "clam":
            return NYStyleClamPizza()
        if item == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None