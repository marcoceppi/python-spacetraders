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

if TYPE_CHECKING:
    from ..models.ship_nav_route_waypoint import ShipNavRouteWaypoint


T = TypeVar("T", bound="ShipNavRoute")


@attr.s(auto_attribs=True)
class ShipNavRoute:
    """The routing information for the ship's most recent transit or current location.

    Attributes:
        destination (ShipNavRouteWaypoint): The destination or departure of a ships nav route.
        departure (ShipNavRouteWaypoint): The destination or departure of a ships nav route.
        departure_time (datetime.datetime): The date time of the ship's departure.
        arrival (datetime.datetime): The date time of the ship's arrival. If the ship is in-transit, this is the
            expected time of arrival.
    """

    destination: "ShipNavRouteWaypoint"
    departure: "ShipNavRouteWaypoint"
    departure_time: datetime.datetime
    arrival: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_nav_route_waypoint import ShipNavRouteWaypoint

        destination = self.destination.to_dict()

        departure = self.departure.to_dict()

        departure_time = self.departure_time.isoformat()

        arrival = self.arrival.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination": destination,
                "departure": departure,
                "departureTime": departure_time,
                "arrival": arrival,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_nav_route_waypoint import ShipNavRouteWaypoint

        d = src_dict.copy()
        destination = ShipNavRouteWaypoint.from_dict(d.pop("destination"))

        departure = ShipNavRouteWaypoint.from_dict(d.pop("departure"))

        departure_time = isoparse(d.pop("departureTime"))

        arrival = isoparse(d.pop("arrival"))

        ship_nav_route = cls(
            destination=destination,
            departure=departure,
            departure_time=departure_time,
            arrival=arrival,
        )

        ship_nav_route.additional_properties = d
        return ship_nav_route

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
