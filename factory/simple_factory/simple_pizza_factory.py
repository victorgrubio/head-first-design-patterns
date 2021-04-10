"""Simple pizza factory to create pizzas"""
# The job of this class is to extract the creation process from main.py
from simple_factory.pizza import Pizza, CheesePizza, PepperoniPizza, ClamPizza, VeggiePizza


class SimplePizzaFactory(object):

  def create_pizza(pizza_type: str) -> Pizza:
    """Creates a pizza based on its type

    Args:
        pizza_type (str): Type of pizza to create

    Returns:
        Pizza: Created pizza
    """
    pizza: Pizza = None

    if pizza_type == "cheese":
      pizza = CheesePizza()
    elif pizza_type == "pepperoni":
      pizza = PepperoniPizza()
    elif pizza_type == "clam":
      pizza = ClamPizza()
    elif pizza_type == "veggie":
      pizza = VeggiePizza()
    
    return pizza