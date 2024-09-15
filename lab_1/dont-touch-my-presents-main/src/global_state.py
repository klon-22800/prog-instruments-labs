import pygame

from src.components.game_status import GameStatus
from src.config import Config


class GlobalState:
    """class for config main screen"""

    GAME_STATE = GameStatus.MAIN_MENU
    SCREEN = None
    SCROLL = 0
    PRESS_Y = 650

    @staticmethod
    def load_main_screen() -> None:
        """set setting for main screen"""
        screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        screen.fill((0, 255, 255))
        GlobalState.SCREEN = screen
