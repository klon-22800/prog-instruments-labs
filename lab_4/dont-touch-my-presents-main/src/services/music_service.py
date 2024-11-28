import random

import pygame

from typing import List

from paths import AUDIO_DIR


class MusicService:
    """class for game sound"""

    @staticmethod
    def get_background_musics() -> List[str]:
        """getting path for sound for background

        Returns:
            List[str]: list of paths
        """
        return [
            AUDIO_DIR / "sleigh_ride.ogg",
            AUDIO_DIR / "merry_christmas.ogg",
            AUDIO_DIR / "here_comes_santa.ogg",
        ]

    @staticmethod
    def get_chop_musics() -> List[str]:
        """getting path for sound for chop moment

        Returns:
            List[str]: list of paths
        """
        return [
            AUDIO_DIR / "chop.wav",
            AUDIO_DIR / "chop_2.wav",
            AUDIO_DIR / "chop_3.wav",
        ]

    @staticmethod
    def get_cheer_musics() -> List[str]:
        """getting path for cheer music

        Returns:
            List[str]: list of paths
        """
        return [
            AUDIO_DIR / "cheer.wav",
            AUDIO_DIR / "cheer_2.wav",
            AUDIO_DIR / "cheer_3.wav",
            AUDIO_DIR / "cheer_4.wav",
        ]

    @staticmethod
    def start_background_music() -> None:
        """function start background music"""
        if pygame.mixer.music.get_busy():
            return

        musics = MusicService.get_background_musics()
        filename = random.choice(musics)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    @staticmethod
    def play_chop_sound() -> None:
        """function start chop music"""
        musics = MusicService.get_chop_musics()
        filename = random.choice(musics)
        chop = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(chop)

    @staticmethod
    def play_score_sound() -> None:
        """function start score music"""
        score_sfx = pygame.mixer.Sound(AUDIO_DIR / "score.wav")
        pygame.mixer.Sound.play(score_sfx)

    @staticmethod
    def play_slap_sound() -> None:
        """function start slap sound"""
        slap_sfx = pygame.mixer.Sound(AUDIO_DIR / "slap.wav")
        pygame.mixer.Sound.play(slap_sfx)

    @staticmethod
    def play_cheer_sound() -> None:
        """function start cheer cound"""
        musics = MusicService.get_cheer_musics()
        filename = random.choice(musics)
        cheer = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(cheer)
