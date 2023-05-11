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
from pydantic import BaseModel, Field

from ..models.ship_nav_flight_mode import ShipNavFlightMode
from ..models.ship_nav_route import ShipNavRoute
from ..models.ship_nav_status import ShipNavStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipNav")


class ShipNav(BaseModel):
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

    system_symbol: str = Field(alias="systemSymbol")
    waypoint_symbol: str = Field(alias="waypointSymbol")
    route: "ShipNavRoute" = Field(alias="route")
    status: ShipNavStatus = Field(alias="status")
    flight_mode: ShipNavFlightMode = ShipNavFlightMode.CRUISE
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
