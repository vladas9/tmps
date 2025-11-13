from domain.models.character import Character


class CharacterBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._name = ""
        self._health = 0
        self._attack = 0
        self._speed = 0

    def from_raw_stats(self, name: str, health: int, attack: int, speed: int) -> "CharacterBuilder":
        self._name = name
        self._health = health
        self._attack = attack
        self._speed = speed
        return self

    def from_adapter(self, adapter) -> "CharacterBuilder":
        self._name = adapter.get_name()
        self._health = adapter.get_health()
        self._attack = adapter.get_attack()
        self._speed = adapter.get_speed()
        return self

    def apply_prototype(self, proto: Character) -> "CharacterBuilder":
        self._health += proto.get_health()
        self._attack += proto.get_attack()

        return self

    def build(self) -> Character:
        ch = Character(self._name, self._health, self._attack, self._speed)
        self.reset()
        return ch
