from enum import Enum


class RegisterJsonBodyFaction(str, Enum):
    COSMIC = "COSMIC"
    DOMINION = "DOMINION"
    GALACTIC = "GALACTIC"
    QUANTUM = "QUANTUM"
    VOID = "VOID"

    def __str__(self) -> str:
        return str(self.value)
