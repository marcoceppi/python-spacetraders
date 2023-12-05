from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.activity_level import ActivityLevel
from ..models.market_trade_good_type import MarketTradeGoodType
from ..models.supply_level import SupplyLevel
from ..models.trade_symbol import TradeSymbol
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketTradeGood")


class MarketTradeGood(BaseModel):
    """
    Attributes:
        symbol (TradeSymbol): The good's symbol.
        type (MarketTradeGoodType): The type of trade good (export, import, or exchange).
        trade_volume (int): This is the maximum number of units that can be purchased or sold at this market in a single
            trade for this good. Trade volume also gives an indication of price volatility. A market with a low trade volume
            will have large price swings, while high trade volume will be more resilient to price changes.
        supply (SupplyLevel): The supply level of a trade good.
        purchase_price (int): The price at which this good can be purchased from the market.
        sell_price (int): The price at which this good can be sold to the market.
        activity (Union[Unset, ActivityLevel]): The activity level of a trade good. If the good is an import, this
            represents how strong consumption is. If the good is an export, this represents how strong the production is for
            the good. When activity is strong, consumption or production is near maximum capacity. When activity is weak,
            consumption or production is near minimum capacity.
    """

    symbol: TradeSymbol = Field(alias="symbol")
    type: MarketTradeGoodType = Field(alias="type")
    trade_volume: int = Field(alias="tradeVolume")
    supply: SupplyLevel = Field(alias="supply")
    purchase_price: int = Field(alias="purchasePrice")
    sell_price: int = Field(alias="sellPrice")
    activity: Union[Unset, ActivityLevel] = Field(UNSET, alias="activity")
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
