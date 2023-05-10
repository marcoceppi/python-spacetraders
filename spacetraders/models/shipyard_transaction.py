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

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipyardTransaction")


@attr.s(auto_attribs=True)
class ShipyardTransaction:
    """
    Attributes:
        waypoint_symbol (str): The symbol of the waypoint where the transaction took place.
        ship_symbol (str): The symbol of the ship that was purchased.
        price (int): The price of the transaction.
        agent_symbol (str): The symbol of the agent that made the transaction.
        timestamp (datetime.datetime): The timestamp of the transaction.
    """

    waypoint_symbol: str
    ship_symbol: str
    price: int
    agent_symbol: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        waypoint_symbol = self.waypoint_symbol
        ship_symbol = self.ship_symbol
        price = self.price
        agent_symbol = self.agent_symbol
        timestamp = self.timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "waypointSymbol": waypoint_symbol,
                "shipSymbol": ship_symbol,
                "price": price,
                "agentSymbol": agent_symbol,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        waypoint_symbol = d.pop("waypointSymbol")

        ship_symbol = d.pop("shipSymbol")

        price = d.pop("price")

        agent_symbol = d.pop("agentSymbol")

        timestamp = isoparse(d.pop("timestamp"))

        shipyard_transaction = cls(
            waypoint_symbol=waypoint_symbol,
            ship_symbol=ship_symbol,
            price=price,
            agent_symbol=agent_symbol,
            timestamp=timestamp,
        )

        shipyard_transaction.additional_properties = d
        return shipyard_transaction

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
