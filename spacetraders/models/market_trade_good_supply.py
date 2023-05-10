from enum import Enum


class MarketTradeGoodSupply(str, Enum):
    ABUNDANT = "ABUNDANT"
    LIMITED = "LIMITED"
    MODERATE = "MODERATE"
    SCARCE = "SCARCE"

    def __str__(self) -> str:
        return str(self.value)
