from enum import Enum


class ShipRole(str, Enum):
    CARRIER = "CARRIER"
    COMMAND = "COMMAND"
    EXCAVATOR = "EXCAVATOR"
    EXPLORER = "EXPLORER"
    FABRICATOR = "FABRICATOR"
    HARVESTER = "HARVESTER"
    HAULER = "HAULER"
    INTERCEPTOR = "INTERCEPTOR"
    PATROL = "PATROL"
    REFINERY = "REFINERY"
    REPAIR = "REPAIR"
    SATELLITE = "SATELLITE"
    SURVEYOR = "SURVEYOR"
    TRANSPORT = "TRANSPORT"

    def __str__(self) -> str:
        return str(self.value)
