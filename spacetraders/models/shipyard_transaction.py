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

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipyardTransaction")


class ShipyardTransaction(BaseModel):
    """
    Attributes:
        waypoint_symbol (str): The symbol of the waypoint where the transaction took place.
        ship_symbol (str): The symbol of the ship that was purchased.
        price (int): The price of the transaction.
        agent_symbol (str): The symbol of the agent that made the transaction.
        timestamp (datetime.datetime): The timestamp of the transaction.
    """

    waypoint_symbol: str = Field(alias="waypointSymbol")
    ship_symbol: str = Field(alias="shipSymbol")
    price: int = Field(alias="price")
    agent_symbol: str = Field(alias="agentSymbol")
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
