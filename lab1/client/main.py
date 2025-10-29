from domain.singleton.game_manager import GameManager
from domain.builder.character_builder import CharacterBuilder
from domain.prototype.character_prototype import BaseCharacter

def main():
    gm1 = GameManager()
    gm2 = GameManager()
    print(gm1 is gm2)  

    hero = (CharacterBuilder()
            .set_name("Arthas")
            .set_class("Paladin")
            .set_weapon("Holy Sword")
            .set_stats(120, 80)
            .build())
    hero.show_info()

    goblin = BaseCharacter("Goblin", "Enemy", "Club", 40, 20)
    goblin_clone = goblin.clone()
    goblin_clone.name = "Goblin Warrior"
    goblin_clone.weapon = "Axe"

    goblin.show_info()
    goblin_clone.show_info()

if __name__ == "__main__":
    main()
