import abc
from weapons import WeaponBehaviour
from characters.greetings import GreetingBehaviour

class Character(abc.ABC):
    
    greeting: GreetingBehaviour
    weapon: WeaponBehaviour

    def __init__():
        pass

    def set_weapon(self, new_weapon: WeaponBehaviour):
        self.weapon = new_weapon

    def set_greeting(self, new_greeting: GreetingBehaviour):
        self.greeting = new_greeting

    def use_weapon(self, character):
        self.weapon.use(character)

    def greet(self):
        self.greeting.greet()

    @abc.abstractmethod
    def display(self):
        pass
