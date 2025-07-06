import sys
from code.const import C_WHITE, C_YELLOW, MENU_OPTIONS, SCORE_POS
from code.dbProxy import DBProxy
from datetime import datetime

import pygame
from pygame.constants import KEYDOWN
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surface = pygame.image.load("./src/assets/ScoreBg.png").convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)

    def save(self, game_mode: str | None, player_score: list[int]):
        pygame.mixer_music.load("./src/assets/Score.mp3")
        pygame.mixer_music.play(-1)
        db_proxy: DBProxy = DBProxy("DBScore")
        name: str = ""

        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            self.score_text(48, "YOU WON!!", C_YELLOW, SCORE_POS["Title"])
            text = "Enter player 1 name (4 characters):"
            score = player_score[0]

            if game_mode == MENU_OPTIONS[0]:
                score: int = player_score[0]
                text = "Enter player name (4 characters):"
            if game_mode == MENU_OPTIONS[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = "Enter team name (4 characters):"
            if game_mode == MENU_OPTIONS[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = "Enter player 1 name (4 characters):"
                else:
                    score = player_score[1]
                    text = "Enter player 2 name (4 characters):"

            self.score_text(24, text, C_WHITE, SCORE_POS["EnterName"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) <= 4:
                        db_proxy.save(
                            {"name": name, "score": score, "date": get_formatted_date()}
                        )
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(20, name, C_WHITE, SCORE_POS["Name"])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load("./src/assets/Score.mp3")
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surface, dest=self.rect)
        self.score_text(48, "TOP 10 SCORE", C_YELLOW, SCORE_POS["Title"])
        self.score_text(
            20, "NAME    SCORE       DATE        ", C_YELLOW, SCORE_POS["Label"]
        )
        db_proxy: DBProxy = DBProxy("DBScore")
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(
                20,
                f"{name}    {score:>05d}       {date}",
                C_YELLOW,
                SCORE_POS[list_score.index(player_score)],
            )
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple
    ) -> None:
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)


def get_formatted_date() -> str:
    current_datetime: datetime = datetime.now()
    current_time: str = current_datetime.strftime("%H:%M")
    current_date: str = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
