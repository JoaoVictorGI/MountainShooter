from code.const import (
    C_RED,
    C_WHITE,
    C_YELLOW,
    GAME_OVER_OPTIONS,
    WIN_HEIGHT,
    WIN_WIDTH,
)

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surface = pygame.image.load("./src/assets/ScoreBg.png").convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)
        self.overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.overlay.fill((0, 0, 0))
        self.overlay.set_alpha(128)
        self.surface.blit(self.overlay, (0, 0))

    def show(self):
        pygame.mixer_music.load("./src/assets/Score.mp3")
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surface, dest=self.rect)
        self.game_over_text(50, "GAME OVER", C_RED, (WIN_WIDTH / 2, 120))
        # game_over = 0
        menu_option = 0

        while True:
            for i in range(len(GAME_OVER_OPTIONS)):
                if i == menu_option:
                    self.game_over_text(
                        20,
                        GAME_OVER_OPTIONS[i],
                        C_YELLOW,
                        ((WIN_WIDTH / 2), 200 + 25 * i),
                    )
                else:
                    self.game_over_text(
                        20,
                        GAME_OVER_OPTIONS[i],
                        C_WHITE,
                        ((WIN_WIDTH / 2), 200 + 25 * i),
                    )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting...")
                    pygame.quit()  # Close the window
                    quit()  # End pygame "process"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(GAME_OVER_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(GAME_OVER_OPTIONS) - 1

                    if event.key == pygame.K_RETURN:
                        return GAME_OVER_OPTIONS[menu_option]

    def game_over_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple
    ) -> None:
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)
