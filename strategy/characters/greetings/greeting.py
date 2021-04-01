import abc

class GreetingBehaviour(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def greet():
        """Display character greeting"""
        raise NotImplementedError