from enum import Enum


class ShipNavFlightMode(str, Enum):
    BURN = "BURN"
    CRUISE = "CRUISE"
    DRIFT = "DRIFT"
    STEALTH = "STEALTH"

    def __str__(self) -> str:
        return str(self.value)
