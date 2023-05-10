from enum import Enum


class ShipRefineJsonBodyProduce(str, Enum):
    ALUMINUM = "ALUMINUM"
    COPPER = "COPPER"
    FUEL = "FUEL"
    GOLD = "GOLD"
    IRON = "IRON"
    MERITIUM = "MERITIUM"
    PLATINUM = "PLATINUM"
    SILVER = "SILVER"
    URANITE = "URANITE"

    def __str__(self) -> str:
        return str(self.value)
