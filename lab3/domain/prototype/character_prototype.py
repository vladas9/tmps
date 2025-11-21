from domain.models.character import Character


class CharacterPrototypeManager:
    def __init__(self):
        self._templates = {
            "warrior": Character("WarriorTemplate", 80, 15, 5),
            "mage": Character("MageTemplate", 40, 25, 7),
        }

    def get_template(self, key: str) -> Character:
        template = self._templates.get(key)
        if not template:
            raise ValueError(f"No template registered for key: {key}")
        return template.clone()
