from enum import Enum


class ShipNavStatus(str, Enum):
    DOCKED = "DOCKED"
    IN_ORBIT = "IN_ORBIT"
    IN_TRANSIT = "IN_TRANSIT"

    def __str__(self) -> str:
        return str(self.value)
