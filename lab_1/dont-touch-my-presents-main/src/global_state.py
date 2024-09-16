import pygame

from src.components.game_status import GameStatus
from src.config import Config


class GlobalState:
    """
    Class for config main screen
    
    Attributes: 
        game_state: current application status
        screen: GUI object
        scroll: parameter for drawing the screen when scrolling
        press_y: parameter for monitoring button presses

    """
    game_state = GameStatus.main_menu
    screen = None
    scroll = 0
    press_y = 650

    @staticmethod
    def load_main_screen() -> None:
        """set setting for main screen"""
        screen = pygame.display.set_mode((Config.width, Config.height))
        screen.fill((0, 255, 255))
        GlobalState.screen = screen
