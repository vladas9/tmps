Creational Design Patterns
==========================

Author: Vadislav Amza
---------------------


Used Design Patterns
--------------------

-   **Singleton** -- ensures only one instance of the Game Manager exists.

-   **Builder** -- constructs complex Character objects step by step.

-   **Prototype** -- allows cloning of existing Character objects instead of creating new ones from scratch.

* * * * *

Implementation
--------------

### Domain: Game Character Creation

The project simulates a small game system where we need to manage characters and enemies.\
Each pattern was chosen for a specific creation scenario:

-   `Singleton` manages a single game manager.

-   `Builder` helps create complex hero objects.

-   `Prototype` clones existing character templates (like enemies).

* * * * *

### **Singleton Pattern**

Ensures only one instance of the `GameManager` exists during runtime.

```python
class GameManager:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.name = "Global Game Manager"
            self._initialized = True

    def get_name(self):
        return self.name
```
* * * * *

### **Builder Pattern**

Used to create complex game characters step by step.

```python
class CharacterBuilder:
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
```

* * * * *

### **Prototype Pattern**

Allows us to duplicate (clone) an existing character instead of creating one from scratch.

```python
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
```

* * * * *

### **Client Code**

All patterns are demonstrated in the main program.

```python
def main():
    gm = GameManager()
    print(gm.get_name())

    hero = (CharacterBuilder()
            .set_name("Arthas")
            .set_class("Paladin")
            .set_weapon("Holy Sword")
            .set_stats(120, 80)
            .build())
    hero.show_info()

    goblin = BaseCharacter("Goblin", "Enemy", "Club", 40, 20)
    goblin_clone = goblin.clone()
    goblin_clone.name = "Goblin Warrior"
    goblin_clone.weapon = "Axe"

    goblin.show_info()
    goblin_clone.show_info()

if __name__ == "__main__":
    main()
```

* * * * *

### Example Output
```bash
Global Game Manager
Character: Arthas (Paladin) with Holy Sword | HP: 120 | STR: 80
Goblin (Enemy) with Club | HP: 40 | STR: 20
Goblin Warrior (Enemy) with Axe | HP: 40 | STR: 20
```
* * * * *

Conclusions 
-----------------------------------

-   The **Singleton** pattern successfully ensures that only one instance of `GameManager` exists, demonstrating global control over the game's state.
-   The **Builder** pattern provides a flexible, readable, and step-by-step way to construct `Character` objects.
-   The **Prototype** pattern enables efficient creation of multiple similar objects using cloning.
-   Together, these patterns demonstrate clear control, flexibility, and efficiency in object creation.
