import pygame

from src.components.game_status import GameStatus
from src.config import Config
from src.game_phases import main_menu_phase, gameplay_phase, exit_game_phase
from src.global_state import GlobalState
from src.services.music_service import MusicService


pygame.init()

FramePerSec = pygame.time.Clock()


def update_game_display() -> None:
    """function updating game display"""
    pygame.display.update()
    FramePerSec.tick(Config.fps)


def main() -> None:
    """function controls the switching of game phases"""
    while True:
        if GlobalState.game_state == GameStatus.main_menu:
            main_menu_phase()
        elif GlobalState.game_state == GameStatus.gammeplay:
            gameplay_phase()
        elif GlobalState.game_state == GameStatus.game_end:
            exit_game_phase()

        MusicService.start_background_music()
        update_game_display()


if __name__ == "__main__":
    main()
