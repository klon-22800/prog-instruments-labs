from enum import Enum


class GameStatus(Enum):
    """
    enums for game status phase

    Attributes:
        main_menu: user is in the main menu
        gameplay: user plays game
        game_end: user quits game
    """
    main_menu = 0
    gammeplay = 1
    game_end = 2
