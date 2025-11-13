from copy import deepcopy


class Character:
    def __init__(self, name: str, health: int, attack: int, speed: int):
        self._name = name
        self._health = health
        self._attack = attack
        self._speed = speed

    def get_name(self) -> str:
        return self._name

    def get_health(self) -> int:
        return max(0, self._health)

    def get_attack(self) -> int:
        return self._attack

    def get_speed(self) -> int:
        return self._speed

    def take_damage(self, amount: int) -> None:
        self._health -= amount

    def clone(self) -> "Character":
        return deepcopy(self)

    def to_dict(self) -> dict:
        return {
            "name": self.get_name(),
            "health": self.get_health(),
            "attack": self.get_attack(),
            "speed": self.get_speed(),
        }

    def __repr__(self) -> str:
        return f"Character({self._name}, hp={self._health}, atk={self._attack}, spd={self._speed})"
