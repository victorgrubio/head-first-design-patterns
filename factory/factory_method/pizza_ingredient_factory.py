"""Pizza Ingredient Factory (interface)"""
import abc
from ingredients import Dough, Sauce, Cheese, Veggies, Pepperoni, Clams

class PizzaIngredientFactory(abc.ABCMeta):


    @abc.abstractclassmethod
    def create_dought(cls) -> Dough:
        """Creates a dough for a Pizza

        Raises:
            NotImplementedError: As interface method, needs to be implemented

        Returns:
            Dough: Dough for pizza
        """
        raise NotImplementedError

    @abc.abstractclassmethod
    def create_sauce(cls) -> Sauce:
        """Creates a sauce for a Pizza

        Raises:
            NotImplementedError: As interface method, needs to be implemented

        Returns:
            Sauce: Sauce for pizza
        """
        pass

    @abc.abstractclassmethod
    def create_cheese(cls) -> Cheese:
        """Creates a cheese for a Pizza

        Raises:
            NotImplementedError: As interface method, needs to be implemented

        Returns:
            Cheese: Cheese for pizza
        """
        raise NotImplementedError

    @abc.abstractclassmethod
    def create_veggies(cls) -> Veggies:
        """Creates a Veggies for a Pizza

        Raises:
            NotImplementedError: As interface method, needs to be implemented

        Returns:
            Veggies: Veggies for pizza
        """
        raise NotImplementedError

    @abc.abstractclassmethod
    def create_pepperoni(cls) -> Pepperoni:
        """Creates a Pepperoni for a Pizza

        Raises:
            NotImplementedError: As interface method, needs to be implemented

        Returns:
            Pepperoni: Pepperoni for pizza
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_clam(cls) -> Clams:
        """Creates a Clams for a Pizza

        Raises:
            NotImplementedError: As interface method, needs to be implemented

        Returns:
            Clams: Clams for pizza
        """
        raise NotImplementedError