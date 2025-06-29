from builtins import len
from code.const import COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, MENU_OPTIONS, WIN_WIDTH

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface


class Menu:
    def __init__(self, window) -> None:
        self.window = window
        self.surface = pygame.image.load("./src/assets/MenuBg.png").convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(
        self,
    ) -> str | None:
        menu_option = 0
        pygame.mixer_music.load("./src/assets/Menu.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(
                        20,
                        MENU_OPTIONS[i],
                        COLOR_YELLOW,
                        ((WIN_WIDTH / 2), 200 + 25 * i),
                    )
                else:
                    self.menu_text(
                        20,
                        MENU_OPTIONS[i],
                        COLOR_WHITE,
                        ((WIN_WIDTH / 2), 200 + 25 * i),
                    )

            pygame.display.flip()

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting...")
                    pygame.quit()  # Close the window
                    quit()  # End pygame "process"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]

    def menu_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple
    ) -> None:
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)
