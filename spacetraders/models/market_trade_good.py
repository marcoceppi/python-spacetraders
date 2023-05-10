from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
)

import attr

from ..models.market_trade_good_supply import MarketTradeGoodSupply
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketTradeGood")


@attr.s(auto_attribs=True)
class MarketTradeGood:
    """
    Attributes:
        symbol (str): The symbol of the trade good.
        trade_volume (int): The typical volume flowing through the market for this type of good. The larger the trade
            volume, the more stable prices will be.
        supply (MarketTradeGoodSupply): A rough estimate of the total supply of this good in the marketplace.
        purchase_price (int): The price at which this good can be purchased from the market.
        sell_price (int): The price at which this good can be sold to the market.
    """

    symbol: str
    trade_volume: int
    supply: MarketTradeGoodSupply
    purchase_price: int
    sell_price: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol
        trade_volume = self.trade_volume
        supply = self.supply.value

        purchase_price = self.purchase_price
        sell_price = self.sell_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "tradeVolume": trade_volume,
                "supply": supply,
                "purchasePrice": purchase_price,
                "sellPrice": sell_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol")

        trade_volume = d.pop("tradeVolume")

        supply = MarketTradeGoodSupply(d.pop("supply"))

        purchase_price = d.pop("purchasePrice")

        sell_price = d.pop("sellPrice")

        market_trade_good = cls(
            symbol=symbol,
            trade_volume=trade_volume,
            supply=supply,
            purchase_price=purchase_price,
            sell_price=sell_price,
        )

        market_trade_good.additional_properties = d
        return market_trade_good

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
