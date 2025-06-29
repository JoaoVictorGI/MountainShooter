from builtins import super
from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass
