import math

import pygame
from pygame.locals import QUIT, K_ESCAPE


def sine(speed: float, time: int, how_far: float, overall_y: int) -> int:
    t = pygame.time.get_ticks() / 2 % time
    y = math.sin(t / speed) * how_far + overall_y
    return int(y)


def update_background_using_scroll(scroll: float) -> float:
    scroll -= 0.5

    if scroll < -80:
        scroll = 0

    return scroll


def update_press_key(press_y: int) -> float:
    if press_y > 460:
        return press_y * 0.99

    return press_y


def is_close_app_event(event: pygame.event.Event) -> bool:
    return (event.type == QUIT) or (
        event.type == pygame.KEYDOWN and event.key == K_ESCAPE
    )
