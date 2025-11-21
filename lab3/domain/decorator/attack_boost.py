from .character_decorator import CharacterDecorator


class AttackBoost(CharacterDecorator):
    def __init__(self, wrapped, bonus: int = 10):
        super().__init__(wrapped)
        self._bonus = bonus

    def get_attack(self) -> int:
        return self._wrapped.get_attack() + self._bonus
