from teams.exceptions import (
    NegativeTitlesError,
    InvalidYearCupError,
    ImpossibleTitlesError,
)
from datetime import datetime


FIRST_CUP: int = 1930


def check_title(titles: int) -> None:
    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")


def check_year(first_cup: str) -> None:
    year = datetime.strptime(first_cup, "%Y-%m-%d")
    if (year.year - FIRST_CUP) % 4 != 0 or year.year < FIRST_CUP:
        raise InvalidYearCupError("there was no world cup this year")


def check_titles_is_possible(titles: int, first_cup: str) -> None:
    first_year = datetime.strptime(first_cup, "%Y-%m-%d").year
    actual_year = datetime.now().year
    if (actual_year - first_year) / 4 < titles:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


def data_processing(selection: dict):

    check_title(selection["titles"])

    check_year(selection["first_cup"])

    check_titles_is_possible(selection["titles"], selection["first_cup"])
