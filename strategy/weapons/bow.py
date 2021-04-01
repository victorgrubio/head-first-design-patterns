from weapons.weapon import WeaponBehaviour


class Bow(WeaponBehaviour):
    
    def use(self, enemy_character):
        print("I am using the arch")