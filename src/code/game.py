from code.const import MENU_OPTIONS, WIN_HEIGHT, WIN_WIDTH
from code.level import Level
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
            menu_return: str | None = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level: Level = Level(self.window, "Level1", menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTIONS[4]:
                pygame.quit()
                quit()
            else:
                pass
