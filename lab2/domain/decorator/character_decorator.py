from domain.models.character import Character


class CharacterDecorator(Character):
    def __init__(self, wrapped: Character):
        self._wrapped = wrapped

    def get_name(self) -> str:
        return self._wrapped.get_name()

    def get_health(self) -> int:
        return self._wrapped.get_health()

    def get_attack(self) -> int:
        return self._wrapped.get_attack()

    def get_speed(self) -> int:
        return self._wrapped.get_speed()

    def take_damage(self, amount: int) -> None:
        self._wrapped.take_damage(amount)

    def to_dict(self) -> dict:
        return self._wrapped.to_dict()
