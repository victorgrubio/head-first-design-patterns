"""Module containing all pizza types"""


class Pizza(object):
    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class CheesePizza(Pizza):
    pass


class PepperoniPizza(Pizza):
    pass


class ClamPizza(Pizza):
    pass


class VeggiePizza(Pizza):
    pass
