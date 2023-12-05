from enum import Enum


class MarketTradeGoodType(str, Enum):
    EXCHANGE = "EXCHANGE"
    EXPORT = "EXPORT"
    IMPORT = "IMPORT"

    def __str__(self) -> str:
        return str(self.value)
