import random
import sys
from code.const import (
    C_CYAN,
    C_GREEN,
    C_WHITE,
    EVENT_ENEMY,
    EVENT_TIMEOUT,
    MENU_OPTIONS,
    SPAWN_TIME,
    TIMEOUT_LEVEL,
    TIMEOUT_STEP,
    WIN_HEIGHT,
)
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player
from typing import Iterable, cast

import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.time import Clock


class Level:
    def __init__(
        self, window: Surface, name: str, game_mode: str | None, player_score: list[int]
    ) -> None:
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []
        self.entity_list.extend(
            cast(Iterable[Entity], EntityFactory.get_entity(f"{self.name}Bg"))
        )
        player = EntityFactory.get_entity("Player1")
        player.score = player_score[0]
        self.entity_list.append(player)
        self.entity_list.append(cast(Entity, EntityFactory.get_entity("Player1")))
        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            player = EntityFactory.get_entity("Player2")
            player.score = player_score[1]
            self.entity_list.append(cast(Entity, EntityFactory.get_entity("Player2")))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self) -> bool | None:
        pygame.mixer_music.load(f"./src/assets/{self.name}.mp3")
        pygame.mixer_music.play(-1)
        while True:
            clock: Clock = pygame.time.Clock()
            for entity in self.entity_list:
                clock.tick(60)
                self.window.blit(source=entity.surface, dest=entity.rect)
                entity.move()
                if isinstance(entity, (Player, Enemy)):
                    shoot = entity.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if entity.name == "Player1":
                    self.level_text(
                        14,
                        f"Player1 - Health: {entity.health} | Score: {entity.score}",
                        C_GREEN,
                        (10, 25),
                    )
                if entity.name == "Player2":
                    self.level_text(
                        14,
                        f"Player2 - Health: {entity.health} | Score: {entity.score}",
                        C_CYAN,
                        (10, 45),
                    )
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice: str = random.choice(("Enemy1", "Enemy2"))
                    self.entity_list.append(
                        cast(Entity, EntityFactory.get_entity(choice))
                    )
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for entity in self.entity_list:
                            if isinstance(entity, Player) and entity.name == "Player1":
                                player_score[0] = entity.score
                            if isinstance(entity, Player) and entity.name == "Player2":
                                player_score[1] = entity.score
                        return True

                found_player = False
                for entity in self.entity_list:
                    if isinstance(entity, Player):
                        found_player = True

                if not found_player:
                    return False

            self.level_text(
                14,
                f"{self.name} - Timeout: {self.timeout / 1000:.1f}",
                C_WHITE,
                (10, 5),
            )
            self.level_text(
                14, f"FPS: {clock.get_fps():.1f}", C_WHITE, (10, WIN_HEIGHT - 35)
            )
            self.level_text(
                14,
                f"Entidades: {len(self.entity_list)}",
                C_WHITE,
                (10, WIN_HEIGHT - 20),
            )
            pygame.display.flip()

            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)
        pass

    def level_text(
        self,
        text_size: int,
        text: str,
        text_color: tuple[int, int, int],
        text_pos: tuple[int, int],
    ):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surface, dest=text_rect)
