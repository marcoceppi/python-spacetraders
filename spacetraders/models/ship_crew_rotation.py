from enum import Enum


class ShipCrewRotation(str, Enum):
    RELAXED = "RELAXED"
    STRICT = "STRICT"

    def __str__(self) -> str:
        return str(self.value)
