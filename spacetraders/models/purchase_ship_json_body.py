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

from ..models.ship_type import ShipType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseShipJsonBody")


@attr.s(auto_attribs=True)
class PurchaseShipJsonBody:
    """
    Attributes:
        ship_type (ShipType):
        waypoint_symbol (str): The symbol of the waypoint you want to purchase the ship at.
    """

    ship_type: ShipType
    waypoint_symbol: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ship_type = self.ship_type.value

        waypoint_symbol = self.waypoint_symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipType": ship_type,
                "waypointSymbol": waypoint_symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ship_type = ShipType(d.pop("shipType"))

        waypoint_symbol = d.pop("waypointSymbol")

        purchase_ship_json_body = cls(
            ship_type=ship_type,
            waypoint_symbol=waypoint_symbol,
        )

        purchase_ship_json_body.additional_properties = d
        return purchase_ship_json_body

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
