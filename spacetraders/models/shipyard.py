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

from ..models.shipyard_ship import ShipyardShip
from ..models.shipyard_ship_types_item import ShipyardShipTypesItem
from ..models.shipyard_transaction import ShipyardTransaction
from ..types import UNSET, Unset

T = TypeVar("T", bound="Shipyard")


class Shipyard(BaseModel):
    """
    Attributes:
        symbol (str): The symbol of the shipyard. The symbol is the same as the waypoint where the shipyard is located.
        ship_types (List['ShipyardShipTypesItem']): The list of ship types available for purchase at this shipyard.
        transactions (Union[Unset, List['ShipyardTransaction']]): The list of recent transactions at this shipyard.
        ships (Union[Unset, List['ShipyardShip']]): The ships that are currently available for purchase at the shipyard.
    """

    symbol: str = Field(alias="symbol")
    ship_types: List["ShipyardShipTypesItem"] = Field(alias="shipTypes")
    transactions: Union[Unset, List["ShipyardTransaction"]] = UNSET
    ships: Union[Unset, List["ShipyardShip"]] = UNSET
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
