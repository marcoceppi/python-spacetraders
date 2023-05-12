from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.market_trade_good_supply import MarketTradeGoodSupply
from ..types import Unset

T = TypeVar("T", bound="MarketTradeGood")


class MarketTradeGood(BaseModel):
    """
    Attributes:
        symbol (str): The symbol of the trade good.
        trade_volume (int): The typical volume flowing through the market for this type of good. The larger the trade
            volume, the more stable prices will be.
        supply (MarketTradeGoodSupply): A rough estimate of the total supply of this good in the marketplace.
        purchase_price (int): The price at which this good can be purchased from the market.
        sell_price (int): The price at which this good can be sold to the market.
    """

    symbol: str = Field(alias="symbol")
    trade_volume: int = Field(alias="tradeVolume")
    supply: MarketTradeGoodSupply = Field(alias="supply")
    purchase_price: int = Field(alias="purchasePrice")
    sell_price: int = Field(alias="sellPrice")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def dict(self, *args, **kwargs):
        output = super().dict(*args, **kwargs)
        return {k: v for k, v in output.items() if not isinstance(v, Unset)}

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
