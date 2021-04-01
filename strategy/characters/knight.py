from characters.greetings import MedievalGreeting
from characters.character import Character
from weapons import Sword

class Knight(Character):

    def __init__(self):
        Knight.weapon = Sword()
        Knight.greeting = MedievalGreeting()

    def display(self):
        print("Here should be an KNIGHT drawn but I am too lazy to do it.")