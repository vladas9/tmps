from abc import ABC, abstractmethod
from typing import List


class Item:
    def __init__(self, name: str, price: int, power: int) -> None:
        self.name: str = name
        self.price: int = price
        self.power: int = power


class Player:
    def __init__(self, name: str, gold: int = 100) -> None:
        self.name: str = name
        self.gold: int = gold
        self.inventory: List[Item] = []

    def buy(self, item: Item, cost: int) -> None:
        if self.gold >= cost:
            self.gold -= cost
            self.inventory.append(item)

    def show_inventory(self) -> None:
        print(f"{self.name}'s Inventory:")
        for i in self.inventory:
            print(f" - {i.name} (+{i.power} power)")
        print(f"Gold left: {self.gold}\n")


class PriceModifier(ABC):
    @abstractmethod
    def modify(self, price: int) -> int:
        pass


class NoDiscount(PriceModifier):
    def modify(self, price: int) -> int:
        return price


class SeasonalDiscount(PriceModifier):
    def __init__(self, percent: float) -> None:
        self.percent: float = percent

    def modify(self, price: int) -> int:
        return int(price * (1 - self.percent / 100))


class VIPDiscount(PriceModifier):
    def modify(self, price: int) -> int:
        return int(price * 0.8)


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, player: Player, amount: int) -> bool:
        pass


class GoldPaymentProcessor(PaymentProcessor):
    def pay(self, player: Player, amount: int) -> bool:
        if player.gold >= amount:
            player.gold -= amount
            return True
        return False


class Shop:
    def __init__(self, items: List[Item], payment_processor: PaymentProcessor, modifier: PriceModifier) -> None:
        self.items: List[Item] = items
        self.payment: PaymentProcessor = payment_processor
        self.modifier: PriceModifier = modifier

    def display_items(self) -> None:
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - {item.price} gold (+{item.power} power)")

    def sell(self, player: Player, item_index: int) -> None:
        item: Item = self.items[item_index - 1]
        final_price: int = self.modifier.modify(item.price)
        if self.payment.pay(player, final_price):
            player.inventory.append(item)


if __name__ == "__main__":
    sword = Item("Sword of Flames", 60, 15)
    shield = Item("Guardian Shield", 40, 8)
    potion = Item("Healing Potion", 20, 5)

    player = Player("Unknown", gold=100)
    discount = SeasonalDiscount(25)
    payment = GoldPaymentProcessor()
    shop = Shop([sword, shield, potion], payment, discount)

    shop.display_items()
    shop.sell(player, 1)
    shop.sell(player, 3)
    player.show_inventory()
