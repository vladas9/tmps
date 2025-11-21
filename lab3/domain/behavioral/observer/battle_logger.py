from typing import Any, Dict, List
from .observer import Observer


class BattleLogger(Observer):

    def __init__(self):
        self.logs: List[str] = []

    def update(self, event_type: str, data: Dict[str, Any]) -> None:
        if event_type == "battle_started":
            c1 = data["char1"].get_name()
            c2 = data["char2"].get_name()
            self.logs.append(f"Battle begins between {c1} and {c2}")

        elif event_type == "attack":
            atk = data["attacker"].get_name()
            df = data["defender"].get_name()
            dmg = data["damage"]
            hp_after = data["defender_hp"]
            self.logs.append(
                f"{atk} hits {df} for {dmg} damage (HP now {hp_after})"
            )

        elif event_type == "battle_finished":
            winner = data["winner"].get_name()
            self.logs.append(f"Winner: {winner}")
