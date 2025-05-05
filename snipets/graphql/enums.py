from typing import List


def choices_to_enum(choices: List[tuple]):
    return {item[0]: item[0] for item in choices}