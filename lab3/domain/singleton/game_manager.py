import time

class GameManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._char1 = None
            cls._instance._char2 = None
        return cls._instance

    def set_character(self, slot, character):
        if slot == 1:
            self._char1 = character
        else:
            self._char2 = character

    def get_character(self, slot):
        return self._char1 if slot == 1 else self._char2

    def simulate_battle_realtime(self, ui_update_callback, sleep_time=0.7):
        logs = []
        ch1 = self._char1
        ch2 = self._char2

        logs.append(f"Battle begins between {ch1.get_name()} and {ch2.get_name()}")
        ui_update_callback(logs[-1], ch1.get_health(), ch2.get_health())
        time.sleep(sleep_time)

        turn = 0
        while ch1.get_health() > 0 and ch2.get_health() > 0:
            attacker = ch1 if turn % 2 == 0 else ch2
            defender = ch2 if turn % 2 == 0 else ch1

            damage = attacker.get_attack()
            defender.take_damage(damage)

            text = (
                f"{attacker.get_name()} hits {defender.get_name()} "
                f"for {damage} damage! (HP now {defender.get_health()})"
            )
            logs.append(text)

            ui_update_callback(text, ch1.get_health(), ch2.get_health())
            time.sleep(sleep_time)

            turn += 1

        winner = ch1 if ch1.get_health() > 0 else ch2
        final_msg = f"Winner: {winner.get_name()}"
        logs.append(final_msg)

        ui_update_callback(final_msg, ch1.get_health(), ch2.get_health())

        return winner, logs
