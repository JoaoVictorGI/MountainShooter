import sys
from code.const import MENU_OPTIONS, WIN_HEIGHT, WIN_WIDTH
from code.gameOver import GameOver
from code.level import Level
from code.menu import Menu
from code.score import Score

import pygame
from pygame.surface import Surface


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window: Surface = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self) -> None:
        while True:
            score: Score = Score(self.window)
            menu: Menu = Menu(self.window)
            menu_return: str | None = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                player_score: list[int] = [0, 0]  # [Player1, Player2]
                level: Level = Level(self.window, "Level1", menu_return, player_score)
                level_return: bool | None = level.run(player_score)
                if not level_return:
                    game_over = GameOver(self.window)
                    game_over_return = game_over.show()
                    if game_over_return == "EXIT":
                        pygame.quit()
                        sys.exit()
                    continue
                level: Level = Level(self.window, "Level2", menu_return, player_score)
                level_return = level.run(player_score)
                if not level_return:
                    game_over = GameOver(self.window)
                    game_over_return = game_over.show()
                    if game_over_return == "EXIT":
                        pygame.quit()
                        sys.exit()
                if level_return:
                    score.save(game_mode=menu_return, player_score=player_score)
            elif menu_return == MENU_OPTIONS[3]:
                score.show()
            elif menu_return == MENU_OPTIONS[4]:
                pygame.quit()
                quit()
            else:
                pygame.quit()
                sys.exit()
