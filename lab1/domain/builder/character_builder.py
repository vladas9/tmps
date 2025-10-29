
from .character import Character

class CharacterBuilder:
    """Builder pattern: constructs Character objects step-by-step."""
    def __init__(self):
        self.name = None
        self.char_class = None
        self.weapon = None
        self.health = 100
        self.strength = 50

    def set_name(self, name):
        self.name = name
        return self

    def set_class(self, char_class):
        self.char_class = char_class
        return self

    def set_weapon(self, weapon):
        self.weapon = weapon
        return self

    def set_stats(self, health, strength):
        self.health = health
        self.strength = strength
        return self

    def build(self):
        return Character(self.name, self.char_class, self.weapon, self.health, self.strength)
