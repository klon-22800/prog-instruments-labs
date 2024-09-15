import random

import pygame

from src.components.hand_side import HandSide
from src.components.hand_state import RightHand, LeftHand, HAND_MAX_SPEED
from src.components.scoreboard import Scoreboard
from src.config import Config
from src.services.music_service import MusicService
from src.services.visualization_service import VisualizationService
from src.utils.tools import sine


class Hand(pygame.sprite.Sprite):
    """class for enemy hands"""

    def __init__(self, hand_side: HandSide) -> None:
        """contructor of Hand class

        Args:
            hand_side (HandSide): consts from HandSide
        """
        super().__init__()
        self.new_spd = random.uniform(2.5, 3)
        self.new_y = 0
        self.offset_x = 0
        self.new_x = sine(100.0, 1280, 20.0, self.offset_x)
        self.side = hand_side
        self.can_score = True

        self._load_hand()

    def reset(self) -> None:
        """function reset game settings"""
        self.new_spd = random.uniform(0.5, HAND_MAX_SPEED)
        self.can_score = True

        if self.side == HandSide.RIGHT:
            self.offset_x = random.randint(
                RightHand.OFFSET_START, RightHand.OFFSET_STOP
            )
            self.new_y = RightHand.START_Y
            self.new_x = RightHand.START_X

        if self.side == HandSide.LEFT:
            self.offset_x = random.randint(LeftHand.OFFSET_START, LeftHand.OFFSET_STOP)
            self.new_y = LeftHand.START_Y
            self.new_x = LeftHand.START_X

    def _load_hand(self) -> None:
        """loading hands image"""
        if self.side == HandSide.RIGHT:
            self._load_right_hand()

        if self.side == HandSide.LEFT:
            self._load_left_hand()

    def _load_left_hand(self) -> None:
        """loading left hand image"""
        self.image = VisualizationService.get_left_hand_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.offset_x = random.randint(LeftHand.OFFSET_START, LeftHand.OFFSET_STOP)
        self.new_y = LeftHand.START_Y

    def _load_right_hand(self) -> None:
        """loading right hand image"""
        self.image = VisualizationService.get_right_hand_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.offset_x = random.randint(RightHand.OFFSET_START, RightHand.OFFSET_STOP)
        self.new_y = RightHand.START_Y

    def move(
        self, scoreboard: Scoreboard, player_position: pygame.math.Vector2
    ) -> None:
        """function to calculate the player's position

        Args:
            scoreboard (Scoreboard): Scoreboard class to display the score
            player_position (pygame.math.Vector2): coordinates vector of position
        """
        self.new_x = sine(100.0, 620, 20.0, self.offset_x)
        self.new_y += self.new_spd
        self.rect.center = (self.new_x, self.new_y)

        if self.rect.top > player_position.y - 35 and self.can_score:
            scoreboard.increase_current_score()
            self.can_score = False

            MusicService.play_score_sound()

            if scoreboard.get_current_score() % 5 == 0:
                MusicService.play_cheer_sound()

        if self.rect.top > Config.HEIGHT:
            self.rect.bottom = 0
            # Play Kung Fu Sound
            self.new_spd = random.uniform(0.5, HAND_MAX_SPEED)

            if self.side == HandSide.RIGHT:
                self.offset_x = random.randint(
                    RightHand.OFFSET_START, RightHand.OFFSET_STOP
                )
                self.new_y = RightHand.START_Y

            if self.side == HandSide.LEFT:
                self.offset_x = random.randint(
                    LeftHand.OFFSET_START, LeftHand.OFFSET_STOP
                )
                self.new_y = LeftHand.START_Y

            if self.new_spd >= 6:
                self.new_spd = HAND_MAX_SPEED
                MusicService.play_chop_sound()

            self.can_score = True

    def draw(self, screen: pygame.Surface) -> None:
        """function for drawing hands

        Args:
            screen (pygame.Surface): game's surface
        """
        dotted_line = VisualizationService.get_dotted_line()
        screen.blit(dotted_line, (0, self.rect.y + 53))
        screen.blit(self.image, self.rect)
