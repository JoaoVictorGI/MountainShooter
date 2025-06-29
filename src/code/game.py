from code.const import WIN_HEIGHT, WIN_WIDTH
from code.menu import Menu

import pygame
from pygame.surface import Surface


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window: Surface = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self) -> None:
        while True:
            menu: Menu = Menu(self.window)
            menu.run()
            pass
