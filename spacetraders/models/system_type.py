from enum import Enum


class SystemType(str, Enum):
    BLACK_HOLE = "BLACK_HOLE"
    BLUE_STAR = "BLUE_STAR"
    HYPERGIANT = "HYPERGIANT"
    NEBULA = "NEBULA"
    NEUTRON_STAR = "NEUTRON_STAR"
    ORANGE_STAR = "ORANGE_STAR"
    RED_STAR = "RED_STAR"
    UNSTABLE = "UNSTABLE"
    WHITE_DWARF = "WHITE_DWARF"
    YOUNG_STAR = "YOUNG_STAR"

    def __str__(self) -> str:
        return str(self.value)
