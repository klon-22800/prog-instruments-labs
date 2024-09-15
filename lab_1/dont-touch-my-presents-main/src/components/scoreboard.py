import pygame

from src.config import Config
from src.services.score_service import ScoreService
from src.services.visualization_service import VisualizationService
from src.utils.tools import sine


class Scoreboard:
    """class for Scoreboard object"""

    def __init__(self) -> None:
        """contructor of Scoreboard class"""
        self._current_score = 0
        self._max_score = ScoreService.get_max_score()

    def reset_current_score(self) -> None:
        """reseting current score"""
        self._current_score = 0

    def increase_current_score(self) -> None:
        """increase score by 1"""
        self._current_score += 1

    def get_max_score(self) -> int:
        """getter for max score

        Returns:
            int: max score
        """
        return self._max_score

    def get_current_score(self) -> int:
        """getter for curent score

        Returns:
            int: current score
        """
        return self._current_score

    def update_max_score(self) -> None:
        """update picture of max score"""
        if self._current_score > self._max_score:
            ScoreService.update_max_score(self._current_score)
            self._max_score = self._current_score

    def draw(self, screen: pygame.Surface) -> None:
        """drawing scoreboard image

        Args:
            screen (pygame.Surface): Surface of game
        """
        y = sine(200.0, 1280, 10.0, 40)
        show_score = VisualizationService.get_main_font().render(
            str(self._current_score), True, (0, 0, 0)
        )
        score_rect = show_score.get_rect(center=(Config.WIDTH // 2, y + 30))
        screen.blit(VisualizationService.get_score_backing(), (113, y))
        screen.blit(show_score, score_rect)
