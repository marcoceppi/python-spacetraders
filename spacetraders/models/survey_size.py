from enum import Enum


class SurveySize(str, Enum):
    LARGE = "LARGE"
    MODERATE = "MODERATE"
    SMALL = "SMALL"

    def __str__(self) -> str:
        return str(self.value)
