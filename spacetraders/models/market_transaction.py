import datetime
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
    cast,
)

import attr
from dateutil.parser import isoparse
from pydantic import BaseModel, Field

from ..models.market_transaction_type import MarketTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketTransaction")


class MarketTransaction(BaseModel):
    """
    Attributes:
        waypoint_symbol (str): The symbol of the waypoint where the transaction took place.
        ship_symbol (str): The symbol of the ship that made the transaction.
        trade_symbol (str): The symbol of the trade good.
        type (MarketTransactionType): The type of transaction.
        units (int): The number of units of the transaction.
        price_per_unit (int): The price per unit of the transaction.
        total_price (int): The total price of the transaction.
        timestamp (datetime.datetime): The timestamp of the transaction.
    """

    waypoint_symbol: str = Field(alias="waypointSymbol")
    ship_symbol: str = Field(alias="shipSymbol")
    trade_symbol: str = Field(alias="tradeSymbol")
    type: MarketTransactionType = Field(alias="type")
    units: int = Field(alias="units")
    price_per_unit: int = Field(alias="pricePerUnit")
    total_price: int = Field(alias="totalPrice")
    timestamp: datetime.datetime = Field(alias="timestamp")
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
