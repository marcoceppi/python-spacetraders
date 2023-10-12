import datetime
from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.ship_nav_route_waypoint import ShipNavRouteWaypoint
from ..types import Unset

T = TypeVar("T", bound="ShipNavRoute")


class ShipNavRoute(BaseModel):
    """The routing information for the ship's most recent transit or current location.

    Attributes:
        destination (ShipNavRouteWaypoint): The destination or departure of a ships nav route.
        departure (ShipNavRouteWaypoint): The destination or departure of a ships nav route.
        origin (ShipNavRouteWaypoint): The destination or departure of a ships nav route.
        departure_time (datetime.datetime): The date time of the ship's departure.
        arrival (datetime.datetime): The date time of the ship's arrival. If the ship is in-transit, this is the
            expected time of arrival.
    """

    destination: "ShipNavRouteWaypoint" = Field(alias="destination")
    departure: "ShipNavRouteWaypoint" = Field(alias="departure")
    origin: "ShipNavRouteWaypoint" = Field(alias="origin")
    departure_time: datetime.datetime = Field(alias="departureTime")
    arrival: datetime.datetime = Field(alias="arrival")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def dict(self, *args, **kwargs):
        output = super().dict(*args, **kwargs)
        return {k: v for k, v in output.items() if not isinstance(v, Unset)}

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
