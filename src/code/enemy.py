from code.const import ENTITY_SPEED
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple[int, int | float]):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
