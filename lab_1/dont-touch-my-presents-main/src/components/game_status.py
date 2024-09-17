from enum import Enum


class GameStatus(Enum):
    """
    enums for game status phase

    Attributes:
        MAIN_MENU: user is in the main menu
        GAMEPLAY: user plays game
        GAME_END: user quits game
    """
    MAIN_MENU = 0
    GAMEPLAY = 1
    GAME_END = 2
