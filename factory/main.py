from pizza import Pizza

def order_pizza(pizza_type: str) -> Pizza:
    pizza = Pizza()
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza