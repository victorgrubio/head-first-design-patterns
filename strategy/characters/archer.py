from characters.greetings import MedievalGreeting
from characters.character import Character
from weapons import Bow

class Archer(Character):

    def __init__(self):
        self.weapon = Bow()
        self.greeting = MedievalGreeting()

    def display():
        print("Here should be an ARCHER drawn but I am too lazy to do it.")