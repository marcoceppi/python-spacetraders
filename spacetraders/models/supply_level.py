from enum import Enum


class SupplyLevel(str, Enum):
    ABUNDANT = "ABUNDANT"
    HIGH = "HIGH"
    LIMITED = "LIMITED"
    MODERATE = "MODERATE"
    SCARCE = "SCARCE"

    def __str__(self) -> str:
        return str(self.value)
