import math

import pygame
from pygame.locals import QUIT, K_ESCAPE


def sine(speed: float, time: int, how_far: float, overall_y: int) -> int:
    """function creates shaking of objects

    Args:
        speed (float): shaking speed
        time (int): ticks of time
        how_far (float): shaking factor
        overall_y (int): y limit coefficient

    Returns:
        int: _description_
    """
    t = pygame.time.get_ticks() / 2 % time
    y = math.sin(t / speed) * how_far + overall_y
    return int(y)


def update_background_using_scroll(scroll: float) -> float:
    """function controll scroll parameter

    Args:
        scroll (float): scroll factor

    Returns:
        float: updated scroll
    """
    scroll -= 0.5

    if scroll < -80:
        scroll = 0

    return scroll


def update_press_key(press_y: int) -> float:
    """function controll press key parameter

    Args:
        press_y (int): press key factor

    Returns:
        float: updated press key factor
    """
    if press_y > 460:
        return press_y * 0.99

    return press_y


def is_close_app_event(event: pygame.event.Event) -> bool:
    """function close game if button pushed

    Args:
        event (pygame.event.Event): main game Event

    Returns:
        bool: close game mark
    """
    return (event.type == QUIT) or (
        event.type == pygame.KEYDOWN and event.key == K_ESCAPE
    )
