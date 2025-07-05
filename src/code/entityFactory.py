import random
from builtins import staticmethod
from code.background import Background
from code.const import WIN_HEIGHT, WIN_WIDTH
from code.enemy import Enemy
from code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(7):  # Number of images in background
                    list_bg.append(Background(f"Level1Bg{i}", (0, 0)))
                    list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))
                return list_bg
            case "Level2Bg":
                list_bg = []
                for i in range(5):  # Number of images in background
                    list_bg.append(Background(f"Level2Bg{i}", (0, 0)))
                    list_bg.append(Background(f"Level2Bg{i}", (WIN_WIDTH, 0)))
                return list_bg
            case "Player1":
                return Player("Player1", (10, WIN_HEIGHT / 2 - 30))
            case "Player2":
                return Player("Player2", (10, WIN_HEIGHT / 2 + 30))
            case "Enemy1":
                return Enemy(
                    "Enemy1", (WIN_HEIGHT + 10, random.randint(40, WIN_HEIGHT - 40))
                )
            case "Enemy2":
                return Enemy(
                    "Enemy2", (WIN_HEIGHT + 10, random.randint(40, WIN_HEIGHT - 40))
                )
