from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple[int, int | float]):
        self.name = name
        self.surface = pygame.image.load(
            "./src/assets/" + name + ".png"
        ).convert_alpha()
        self.rect = self.surface.get_rect(left=position[0], top=position[1])
        self.speed: int = 0

    @abstractmethod
    def move(self):
        pass
