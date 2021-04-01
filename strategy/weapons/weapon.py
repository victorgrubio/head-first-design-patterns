import abc

class Weapon(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def use(self):
        """Use the weapon to cause damage"""
        raise NotImplementedError
