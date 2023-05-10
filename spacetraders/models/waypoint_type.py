from enum import Enum


class WaypointType(str, Enum):
    ASTEROID_FIELD = "ASTEROID_FIELD"
    DEBRIS_FIELD = "DEBRIS_FIELD"
    GAS_GIANT = "GAS_GIANT"
    GRAVITY_WELL = "GRAVITY_WELL"
    JUMP_GATE = "JUMP_GATE"
    MOON = "MOON"
    NEBULA = "NEBULA"
    ORBITAL_STATION = "ORBITAL_STATION"
    PLANET = "PLANET"

    def __str__(self) -> str:
        return str(self.value)
