from .character_decorator import CharacterDecorator


class ShieldBoost(CharacterDecorator):
    def __init__(self, wrapped, shield: int = 20):
        super().__init__(wrapped)
        self._shield = shield

    def get_health(self) -> int:
        return max(0, self._wrapped.get_health() + self._shield)
