from enum import Enum


class ShipReactorSymbol(str, Enum):
    REACTOR_ANTIMATTER_I = "REACTOR_ANTIMATTER_I"
    REACTOR_CHEMICAL_I = "REACTOR_CHEMICAL_I"
    REACTOR_FISSION_I = "REACTOR_FISSION_I"
    REACTOR_FUSION_I = "REACTOR_FUSION_I"
    REACTOR_SOLAR_I = "REACTOR_SOLAR_I"

    def __str__(self) -> str:
        return str(self.value)
