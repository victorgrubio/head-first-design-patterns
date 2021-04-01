from characters.greetings import GreetingBehaviour


class MedievalGreeting(GreetingBehaviour):

    @classmethod
    def greet(cls):
        print("- Thanks for choosing me to defend you, your Highness. I won't let you down.")