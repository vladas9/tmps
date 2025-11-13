from typing import Tuple, List, Optional

from domain.singleton import GameManager
from domain.builder import CharacterBuilder
from domain.prototype import CharacterPrototypeManager
from domain.adapter import JSONCharacterAdapter
from domain.decorator import AttackBoost, ShieldBoost
from domain.models import Character


class GameFacade:
    def __init__(self):
        self._manager = GameManager()
        self._builder = CharacterBuilder()
        self._prototypes = CharacterPrototypeManager()

    # -------- Character creation --------

    def load_character_from_json(self, slot: int, json_data: dict, proto_key: str = "warrior") -> Character:
        adapter = JSONCharacterAdapter(json_data)
        proto = self._prototypes.get_template(proto_key)

        character = (
            self._builder
            .from_adapter(adapter)
            .apply_prototype(proto)
            .build()
        )

        self._manager.set_character(slot, character)
        return character

    def get_character(self, slot: int) -> Optional[Character]:
        return self._manager.get_character(slot)

    # -------- Buffs (decorators) --------

    def apply_attack_boost(self, slot: int, bonus: int = 10) -> Character:
        ch = self._manager.get_character(slot)
        if ch is None:
            raise RuntimeError(f"No character in slot {slot}")
        boosted = AttackBoost(ch, bonus)
        self._manager.set_character(slot, boosted)
        return boosted

    def apply_shield_boost(self, slot: int, shield: int = 20) -> Character:
        ch = self._manager.get_character(slot)
        if ch is None:
            raise RuntimeError(f"No character in slot {slot}")
        boosted = ShieldBoost(ch, shield)
        self._manager.set_character(slot, boosted)
        return boosted

    # -------- Battle --------

    def run_battle_realtime(self, ui_callback, sleep_time=0.7):
        return self._manager.simulate_battle_realtime(ui_callback, sleep_time)
