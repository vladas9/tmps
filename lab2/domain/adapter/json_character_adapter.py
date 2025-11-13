class JSONCharacterAdapter:
    def __init__(self, json_data: dict):
        self._data = json_data

    def get_name(self) -> str:
        return self._data["name"]

    def get_health(self) -> int:
        return int(self._data["stats"]["health"])

    def get_attack(self) -> int:
        return int(self._data["stats"]["attack"])

    def get_speed(self) -> int:
        return int(self._data["stats"]["speed"])
