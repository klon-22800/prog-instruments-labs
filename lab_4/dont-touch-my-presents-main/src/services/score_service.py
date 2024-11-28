import json

from paths import ROOT_DIR
from src.logging import logger

score_file_path = ROOT_DIR / "best_score.json"
default_data = {"best": 0}


class ScoreService:
    """class for control and save player score"""

    @staticmethod
    def create_score_file_if_not_exist() -> None:
        """function create file if it not exist"""
        if score_file_path.exists():
            return

        ScoreService.update_score_file(default_data)

    @staticmethod
    def load_score_file() -> dict:
        """loading score file

        Returns:
            dict: .json file for writting score
        """
        with open(score_file_path, mode="r", encoding="utf-8-sig") as file:
            return json.loads(file.read())

    @staticmethod
    def get_max_score() -> int:
        """get max score from .json file

        Returns:
            int: max score
        """
        ScoreService.create_score_file_if_not_exist()
        data = ScoreService.load_score_file()

        return data.get("best")

    @staticmethod
    def update_score_file(data: dict) -> None:
        """updatting .json file of scores

        Args:
            data (dict): score for writting
        """
        with open(score_file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file)

    @staticmethod
    def update_max_score(new_score: int) -> None:
        """function update score and write to file

        Args:
            new_score (int): new max score
        """
        data = ScoreService.load_score_file()
        data["best"] = new_score
        ScoreService.update_score_file(data)
