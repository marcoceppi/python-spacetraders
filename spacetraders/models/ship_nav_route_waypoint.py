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

from ..models.waypoint_type import WaypointType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipNavRouteWaypoint")


@attr.s(auto_attribs=True)
class ShipNavRouteWaypoint:
    """The destination or departure of a ships nav route.

    Attributes:
        symbol (str):
        type (WaypointType): The type of waypoint.
        system_symbol (str):
        x (int):
        y (int):
    """

    symbol: str
    type: WaypointType
    system_symbol: str
    x: int
    y: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol
        type = self.type.value

        system_symbol = self.system_symbol
        x = self.x
        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "type": type,
                "systemSymbol": system_symbol,
                "x": x,
                "y": y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol")

        type = WaypointType(d.pop("type"))

        system_symbol = d.pop("systemSymbol")

        x = d.pop("x")

        y = d.pop("y")

        ship_nav_route_waypoint = cls(
            symbol=symbol,
            type=type,
            system_symbol=system_symbol,
            x=x,
            y=y,
        )

        ship_nav_route_waypoint.additional_properties = d
        return ship_nav_route_waypoint

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
