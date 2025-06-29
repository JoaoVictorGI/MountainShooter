from builtins import staticmethod
from code.background import Background
from code.const import WIN_WIDTH
from code.entity import Entity
from typing import Iterable


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)) -> Iterable[Entity] | None:
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f"Level1Bg{i}", (0, 0)))
                    list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))
                return list_bg
