# Game Shop — SOLID Principles in Python

This project demonstrates three key SOLID principles — **Single Responsibility (S)**, **Open/Closed (O)**, and **Dependency Inversion (D)** — using a simple game shop example.

The shop allows a player to buy items such as swords or potions, while applying discounts and processing payments. Each class follows a distinct responsibility to illustrate clean, modular software design.

---

## Overview

The project simulates a small in-game shop that follows SOLID design principles.

## Principles Demonstrated

### 1. Single Responsibility Principle (S)

> A class should have only one reason to change.

Each class is responsible for one specific function in the system.

**Example:**
```python
class Player:
    def __init__(self, name, gold=100):
        self.name = name
        self.gold = gold
        self.inventory = []

    def buy(self, item, cost):
        if self.gold >= cost:
            self.gold -= cost
            self.inventory.append(item)

```

- The Player class manages only inventory and gold.
- It does not handle payment logic or discount calculations.
- This separation keeps the code modular and easier to maintain.

---

### 2. Open/Closed Principle (O)
> Software entities should be open for extension but closed for modification.

The Shop class supports flexible pricing by using the PriceModifier abstraction.
New discount types can be added without modifying existing code.

#### Example:
```python
class PriceModifier(ABC):
    @abstractmethod
    def modify(self, price): pass

class SeasonalDiscount(PriceModifier):
    def __init__(self, percent):
        self.percent = percent
    def modify(self, price):
        return int(price * (1 - self.percent / 100))
```

- You can add new discount types such as VIPDiscount or WeekendDiscount without changing the Shop implementation.
- The design is open to new functionality but closed to risky code changes.

---

### 3. Dependency Inversion Principle (D)

> High-level modules should not depend on low-level modules. Both should depend on abstractions

The Shop class does not depend directly on specific payment methods.
Instead, it works with the abstract PaymentProcessor interface.

#### Example:

```python
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, player, amount): pass

class GoldPaymentProcessor(PaymentProcessor):
    def pay(self, player, amount):
        if player.gold >= amount:
            player.gold -= amount
            return True
        return False
```

- The shop can work with any payment method by implementing the PaymentProcessor interface.
- This reduces coupling and allows flexible substitution of payment systems (e.g., gems, credit, or coins).

## Key Takeaway
By applying S, O, and D, the project achieves clear separation of concerns, easy extension of features, and low coupling between components.
