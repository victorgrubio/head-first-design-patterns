# Strategy Pattern - Fight Simulator
This is a fight simulator to illustrate the Strategy Pattern applied to characters and weapons.

This development is inspired from the book 'Head First Design Patterns'(LINK) from O'Reilly.

## Table of Contents
  - [Definition](#definition)
  - [Strategy Pattern applied](#strategy-pattern-applied)
  - [Fighting script (main)](#fighting-script-main)
  - [TO-DO](#to-do)


## Definition

The strategy pattern groups different behaviours into an interface, and then define multiple classes
that implement this behaviour in multiple ways. 


## Strategy Pattern applied

In this development, we have created two different interfaces: 

* Weapon (FILE)
* Greeting (FILE)


For example, a greeting message from a character differs depending if it is a Western or a Medieval character. To generalize this, we have created the Greeting Behaviour 'interface' that contains a greet method. 
```python
import abc

class GreetingBehaviour(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def greet():
        """Display character greeting"""
        raise NotImplementedError
```

This method needs to be defined to all clases that implement this behaviour. Our character will use a different greeting depending on their correspondent epoch. A medieval character will have the Medieval Greeting as follows:

```python
from characters.greetings import GreetingBehaviour


class MedievalGreeting(GreetingBehaviour):

    @classmethod
    def greet(cls):
        print("- Thanks for choosing me to defend you, your Highness. I won't let you down.")
```

Finally, our Character class will implement the Weapon and Greetings Behaviour to create our characters. This Class is abstract as we will have personalized warriors based on the different Greetings and Weapons created.

```python
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

```

To complete the implementation, we have created some custom characters for the players to use. After that, this is a fighting simulator, isn't it? Let me show you the Archer:


```python
from characters.greetings import MedievalGreeting
from characters.character import Character
from weapons import Bow

class Archer(Character):

    def __init__(self):
        self.weapon = Bow()
        self.greeting = MedievalGreeting()

    def display(self):
        print("Here should be an ARCHER drawn but I am too lazy to do it.")
```

As can be observed, we only have to declare its custom weapon and greeting. We have defined it in the constructor, although we can assign them using the *set_weapon* and *set_greeting* methods, respectively.

## Fighting script (main)

To check that everything is working properly and have some fun, I have created a simple fighting program. 

Is oriented to two players, each of them can select a characters using input numbers from keyboard. Characters will greet the player with the appropiate message.

After the player selection phase, a coin is tossed to define which player will hit first. 

When one of the characters Health Points are reduced to 0, the winning one will shout a victory message.

A lot of improvement can be done as described in my TO-DO section. Please feel free to fork the project and develop your own game. 

Hope you have learnt something reading this! 

Greetings,

Victor Garcia Rubio 




## TO-DO
1. Create a list of weapons with damage and reload time

2. Create a list of characters with a weapon and a health power

3. Create a fighting script

    3.1. Show character info

    3.2. Select player one and player two characters.

    3.3 Fight and show the winner

4. IMPROVEMENTS

    4.1 Create a miss percentage based on health/weapon dmg/reload time to balance the game and some variability.