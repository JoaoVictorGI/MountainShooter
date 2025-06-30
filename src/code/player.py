from code.const import (
    ENTITY_SPEED,
    PLAYER_KEY_DOWN,
    PLAYER_KEY_LEFT,
    PLAYER_KEY_RIGHT,
    PLAYER_KEY_UP,
    WIN_HEIGHT,
    WIN_WIDTH,
)
from code.entity import Entity

import pygame
from pygame.key import ScancodeWrapper


class Player(Entity):
    def __init__(self, name: str, position: tuple[int, int | float]):
        super().__init__(name, position)

    def update(self):
        pass

    def move(self):
        pressed_key: ScancodeWrapper = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass
