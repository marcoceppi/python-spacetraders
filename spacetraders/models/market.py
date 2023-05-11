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
    Union,
    cast,
)

import attr
from pydantic import BaseModel, Field

from ..models.market_trade_good import MarketTradeGood
from ..models.market_transaction import MarketTransaction
from ..models.trade_good import TradeGood
from ..types import UNSET, Unset

T = TypeVar("T", bound="Market")


class Market(BaseModel):
    """
    Attributes:
        symbol (str): The symbol of the market. The symbol is the same as the waypoint where the market is located.
        exports (List['TradeGood']): The list of goods that are exported from this market.
        imports (List['TradeGood']): The list of goods that are sought as imports in this market.
        exchange (List['TradeGood']): The list of goods that are bought and sold between agents at this market.
        transactions (Union[Unset, List['MarketTransaction']]): The list of recent transactions at this market. Visible
            only when a ship is present at the market.
        trade_goods (Union[Unset, List['MarketTradeGood']]): The list of goods that are traded at this market. Visible
            only when a ship is present at the market.
    """

    symbol: str = Field(alias="symbol")
    exports: List["TradeGood"] = Field(alias="exports")
    imports: List["TradeGood"] = Field(alias="imports")
    exchange: List["TradeGood"] = Field(alias="exchange")
    transactions: Union[Unset, List["MarketTransaction"]] = UNSET
    trade_goods: Union[Unset, List["MarketTradeGood"]] = UNSET
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True

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
