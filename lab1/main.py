from abc import ABC, abstractmethod

class Item:
    def __init__(self, name, price, power):
        self.name = name
        self.price = price
        self.power = power


# ====== Single Responsibility ======
class Player:
    def __init__(self, name, gold=100):
        self.name = name
        self.gold = gold
        self.inventory = []

    def buy(self, item, cost):
        if self.gold >= cost:
            self.gold -= cost
            self.inventory.append(item)

    def show_inventory(self):
        print(f"{self.name}'s Inventory:")
        for i in self.inventory:
            print(f" - {i.name} (+{i.power} power)")
        print(f"Gold left: {self.gold}\n")


# ====== Open/Closed ======
class PriceModifier(ABC):
    @abstractmethod
    def modify(self, price: int) -> int:
        pass

class NoDiscount(PriceModifier):
    def modify(self, price): 
        return price

class SeasonalDiscount(PriceModifier):
    def __init__(self, percent):
        self.percent = percent
    def modify(self, price): 
        return int(price * (1 - self.percent / 100))

class VIPDiscount(PriceModifier):
    def modify(self, price): 
        return int(price * 0.8)


# ====== Dependency Inversion ======
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, player: Player, amount: int) -> bool:
        pass

class GoldPaymentProcessor(PaymentProcessor):
    def pay(self, player, amount):
        if player.gold >= amount:
            player.gold -= amount
            return True
        return False


class Shop:
    def __init__(self, items, payment_processor, modifier):
        self.items = items
        self.payment = payment_processor
        self.modifier = modifier

    def display_items(self):
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - {item.price} gold (+{item.power} power)")
        print()

    def sell(self, player, item_index):
        item = self.items[item_index - 1]
        final_price = self.modifier.modify(item.price)
        if self.payment.pay(player, final_price):
            player.inventory.append(item)


if __name__ == "__main__":
    sword = Item("Sword of Flames", 60, 15)
    shield = Item("Guardian Shield", 40, 8)
    potion = Item("Healing Potion", 20, 5)

    player = Player("Arthas", gold=100)
    discount = SeasonalDiscount(25)
    payment = GoldPaymentProcessor()
    shop = Shop([sword, shield, potion], payment, discount)

    shop.display_items()
    shop.sell(player, 1)
    shop.sell(player, 3)

    player.show_inventory()
