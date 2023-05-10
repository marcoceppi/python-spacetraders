from enum import Enum


class ShipMountDepositsItem(str, Enum):
    ALUMINUM_ORE = "ALUMINUM_ORE"
    AMMONIA_ICE = "AMMONIA_ICE"
    COPPER_ORE = "COPPER_ORE"
    DIAMONDS = "DIAMONDS"
    GOLD_ORE = "GOLD_ORE"
    ICE_WATER = "ICE_WATER"
    IRON_ORE = "IRON_ORE"
    MERITIUM_ORE = "MERITIUM_ORE"
    PLATINUM_ORE = "PLATINUM_ORE"
    PRECIOUS_STONES = "PRECIOUS_STONES"
    QUARTZ_SAND = "QUARTZ_SAND"
    SILICON_CRYSTALS = "SILICON_CRYSTALS"
    SILVER_ORE = "SILVER_ORE"
    URANITE_ORE = "URANITE_ORE"

    def __str__(self) -> str:
        return str(self.value)
