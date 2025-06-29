from code.menu import Menu

import pygame
from pygame.surface import Surface


class Game:
    def __init__(self):
        pygame.init()
        self.window: Surface = pygame.display.set_mode(size=(640, 480))

    def run(
        self,
    ):
        while True:
            menu: Menu = Menu(self.window)
            menu.run()
            pass

        # while True:
        #     # Check for events
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             print("Quitting...")
        #             pygame.quit()  # Close the window
        #             quit()  # End pygame "process"
