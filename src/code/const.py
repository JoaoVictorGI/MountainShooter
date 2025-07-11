from typing import Literal

import pygame

# C
C_ORANGE: tuple[int, int, int] = (255, 128, 0)
C_WHITE: tuple[int, int, int] = (255, 255, 255)
C_YELLOW: tuple[int, int, int] = (255, 255, 0)
C_GREEN: tuple[int, int, int] = (0, 128, 0)
C_CYAN: tuple[int, int, int] = (0, 128, 128)
C_RED: tuple[int, int, int] = (139, 0, 0)

# E
EVENT_ENEMY: int = pygame.USEREVENT + 1

EVENT_TIMEOUT: int = pygame.USEREVENT + 2

ENTITY_SPEED: dict[str, int] = {
    "Level1Bg0": 0,
    "Level1Bg1": 1,
    "Level1Bg2": 2,
    "Level1Bg3": 3,
    "Level1Bg4": 4,
    "Level1Bg5": 5,
    "Level1Bg6": 6,
    "Level2Bg0": 0,
    "Level2Bg1": 1,
    "Level2Bg2": 2,
    "Level2Bg3": 3,
    "Level2Bg4": 4,
    "Player1": 3,
    "Player2": 3,
    "Enemy1": 1,
    "Enemy2": 1,
    "Player1Shot": 1,
    "Player2Shot": 3,
    "Enemy1Shot": 3,
    "Enemy2Shot": 3,
}

ENTITY_HEALTH: dict[str, int] = {
    "Level1Bg0": 99999,
    "Level1Bg1": 99999,
    "Level1Bg2": 99999,
    "Level1Bg3": 99999,
    "Level1Bg4": 99999,
    "Level1Bg5": 99999,
    "Level1Bg6": 99999,
    "Level2Bg0": 99999,
    "Level2Bg1": 99999,
    "Level2Bg2": 99999,
    "Level2Bg3": 99999,
    "Level2Bg4": 99999,
    "Player1": 300,
    "Player2": 300,
    "Enemy1": 50,
    "Enemy2": 60,
    "Player1Shot": 1,
    "Player2Shot": 2,
    "Enemy1Shot": 5,
    "Enemy2Shot": 2,
}

ENTITY_SHOT_DELAY: dict[str, int] = {
    "Player1": 20,
    "Player2": 15,
    "Enemy1": 100,
    "Enemy2": 200,
}

ENTITY_DAMAGE: dict[str, int] = {
    "Level1Bg0": 0,
    "Level1Bg1": 0,
    "Level1Bg2": 0,
    "Level1Bg3": 0,
    "Level1Bg4": 0,
    "Level1Bg5": 0,
    "Level1Bg6": 0,
    "Level2Bg0": 0,
    "Level2Bg1": 0,
    "Level2Bg2": 0,
    "Level2Bg3": 0,
    "Level2Bg4": 0,
    "Player1": 1,
    "Player2": 1,
    "Enemy1": 1,
    "Enemy2": 1,
    "Player1Shot": 25,
    "Player2Shot": 20,
    "Enemy1Shot": 20,
    "Enemy2Shot": 15,
}

ENTITY_SCORE = {
    "Level1Bg0": 0,
    "Level1Bg1": 0,
    "Level1Bg2": 0,
    "Level1Bg3": 0,
    "Level1Bg4": 0,
    "Level1Bg5": 0,
    "Level1Bg6": 0,
    "Level2Bg0": 0,
    "Level2Bg1": 0,
    "Level2Bg2": 0,
    "Level2Bg3": 0,
    "Level2Bg4": 0,
    "Player1": 0,
    "Player2": 0,
    "Enemy1": 100,
    "Enemy2": 125,
    "Player1Shot": 0,
    "Player2Shot": 0,
    "Enemy1Shot": 0,
    "Enemy2Shot": 0,
}

# G
GAME_OVER_OPTIONS: tuple[Literal["MENU"], Literal["EXIT"]] = (
    "MENU",
    "EXIT",
)


# M
MENU_OPTIONS: tuple[str, ...] = (
    "NEW GAME 1P",
    "NEW GAME 2P - COOPERATIVE",
    "NEW GAME 2P - COOPERATIVE",
    "SCORE",
    "EXIT",
)

# P
PLAYER_KEY_UP: dict[str, int] = {"Player1": pygame.K_UP, "Player2": pygame.K_w}
PLAYER_KEY_DOWN: dict[str, int] = {"Player1": pygame.K_DOWN, "Player2": pygame.K_s}
PLAYER_KEY_LEFT: dict[str, int] = {"Player1": pygame.K_LEFT, "Player2": pygame.K_a}
PLAYER_KEY_RIGHT: dict[str, int] = {"Player1": pygame.K_RIGHT, "Player2": pygame.K_d}
PLAYER_KEY_SHOOT: dict[str, int] = {
    "Player1": pygame.K_RCTRL,
    "Player2": pygame.K_LCTRL,
}

# S
SPAWN_TIME: int = 2500

# T
TIMEOUT_STEP: int = 100
TIMEOUT_LEVEL: int = 20000

# W
WIN_WIDTH: int = 576
WIN_HEIGHT: int = 324

# S
SCORE_POS: dict[int | str, tuple[float, int]] = {
    "Title": (WIN_WIDTH / 2, 50),
    "EnterName": (WIN_WIDTH / 2, 80),
    "Label": (WIN_WIDTH / 2, 90),
    "Name": (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}
