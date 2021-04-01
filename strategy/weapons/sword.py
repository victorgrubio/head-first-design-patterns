from weapons.weapon import WeaponBehaviour


class Sword(WeaponBehaviour):
    
    def use(self, enemy_character):
        print("I am using the sword")