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

from ..models.ship_nav_flight_mode import ShipNavFlightMode
from ..models.ship_nav_status import ShipNavStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ship_nav_route import ShipNavRoute


T = TypeVar("T", bound="ShipNav")


@attr.s(auto_attribs=True)
class ShipNav:
    """The navigation information of the ship.

    Attributes:
        system_symbol (str): The system symbol of the ship's current location.
        waypoint_symbol (str): The waypoint symbol of the ship's current location, or if the ship is in-transit, the
            waypoint symbol of the ship's destination.
        route (ShipNavRoute): The routing information for the ship's most recent transit or current location.
        status (ShipNavStatus): The current status of the ship
        flight_mode (ShipNavFlightMode): The ship's set speed when traveling between waypoints or systems. Default:
            ShipNavFlightMode.CRUISE.
    """

    system_symbol: str
    waypoint_symbol: str
    route: "ShipNavRoute"
    status: ShipNavStatus
    flight_mode: ShipNavFlightMode = ShipNavFlightMode.CRUISE
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_nav_route import ShipNavRoute

        system_symbol = self.system_symbol
        waypoint_symbol = self.waypoint_symbol
        route = self.route.to_dict()

        status = self.status.value

        flight_mode = self.flight_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "systemSymbol": system_symbol,
                "waypointSymbol": waypoint_symbol,
                "route": route,
                "status": status,
                "flightMode": flight_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_nav_route import ShipNavRoute

        d = src_dict.copy()
        system_symbol = d.pop("systemSymbol")

        waypoint_symbol = d.pop("waypointSymbol")

        route = ShipNavRoute.from_dict(d.pop("route"))

        status = ShipNavStatus(d.pop("status"))

        flight_mode = ShipNavFlightMode(d.pop("flightMode"))

        ship_nav = cls(
            system_symbol=system_symbol,
            waypoint_symbol=waypoint_symbol,
            route=route,
            status=status,
            flight_mode=flight_mode,
        )

        ship_nav.additional_properties = d
        return ship_nav

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
