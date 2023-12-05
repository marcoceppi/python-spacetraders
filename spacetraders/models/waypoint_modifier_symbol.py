from enum import Enum


class WaypointModifierSymbol(str, Enum):
    CIVIL_UNREST = "CIVIL_UNREST"
    CRITICAL_LIMIT = "CRITICAL_LIMIT"
    RADIATION_LEAK = "RADIATION_LEAK"
    STRIPPED = "STRIPPED"
    UNSTABLE = "UNSTABLE"

    def __str__(self) -> str:
        return str(self.value)
