import random
import sys
from code.const import COLOR_WHITE, EVENT_ENEMY, MENU_OPTIONS, SPAWN_TIME, WIN_HEIGHT
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
    def __init__(self, window: Surface, name: str, game_mode: str | None) -> None:
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(
            cast(Iterable[Entity], EntityFactory.get_entity("Level1Bg"))
        )
        self.entity_list.append(cast(Entity, EntityFactory.get_entity("Player1")))
        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(cast(Entity, EntityFactory.get_entity("Player2")))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice: str = random.choice(("Enemy1", "Enemy2"))
                    self.entity_list.append(
                        cast(Entity, EntityFactory.get_entity(choice))
                    )

            self.level_text(
                14,
                f"{self.name} - Timeout: {self.timeout / 1000:.1f}",
                COLOR_WHITE,
                (10, 5),
            )
            self.level_text(
                14, f"FPS: {clock.get_fps():.1f}", COLOR_WHITE, (10, WIN_HEIGHT - 35)
            )
            self.level_text(
                14,
                f"Entidades: {len(self.entity_list)}",
                COLOR_WHITE,
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
