from enum import Enum


class ActivityLevel(str, Enum):
    GROWING = "GROWING"
    RESTRICTED = "RESTRICTED"
    STRONG = "STRONG"
    WEAK = "WEAK"

    def __str__(self) -> str:
        return str(self.value)
