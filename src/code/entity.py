from abc import ABC, abstractmethod
from code.const import ENTITY_DAMAGE, ENTITY_HEALTH, ENTITY_SCORE

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple[int, int | float]):
        self.name = name
        self.surface = pygame.image.load(
            "./src/assets/" + name + ".png"
        ).convert_alpha()
        self.rect = self.surface.get_rect(left=position[0], top=position[1])
        self.speed: int = 0
        self.health: int = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = "None"
        self.score = ENTITY_SCORE[self.name]

    @abstractmethod
    def move(self):
        pass
