from enum import Enum


class ShipEngineSymbol(str, Enum):
    ENGINE_HYPER_DRIVE_I = "ENGINE_HYPER_DRIVE_I"
    ENGINE_IMPULSE_DRIVE_I = "ENGINE_IMPULSE_DRIVE_I"
    ENGINE_ION_DRIVE_I = "ENGINE_ION_DRIVE_I"
    ENGINE_ION_DRIVE_II = "ENGINE_ION_DRIVE_II"

    def __str__(self) -> str:
        return str(self.value)
