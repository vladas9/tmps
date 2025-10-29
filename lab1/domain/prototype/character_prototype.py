import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class BaseCharacter(Prototype):
    def __init__(self, name, char_class, weapon, health, strength):
        self.name = name
        self.char_class = char_class
        self.weapon = weapon
        self.health = health
        self.strength = strength

    def show_info(self):
        print(f"{self.name} ({self.char_class}) with {self.weapon} | "
              f"HP: {self.health} | STR: {self.strength}")
