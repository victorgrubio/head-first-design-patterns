import abc

class WeaponBehaviour(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def use(self, enemy_character):
        """Use the weapon to cause damage to another character"""
        raise NotImplementedError
