from enum import Enum


class MarketTransactionType(str, Enum):
    PURCHASE = "PURCHASE"
    SELL = "SELL"

    def __str__(self) -> str:
        return str(self.value)
