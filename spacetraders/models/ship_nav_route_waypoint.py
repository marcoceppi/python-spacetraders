from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.waypoint_type import WaypointType
from ..types import Unset

T = TypeVar("T", bound="ShipNavRouteWaypoint")


class ShipNavRouteWaypoint(BaseModel):
    """The destination or departure of a ships nav route.

    Attributes:
        symbol (str): The symbol of the waypoint.
        type (WaypointType): The type of waypoint.
        system_symbol (str): The symbol of the system the waypoint is in.
        x (int): Position in the universe in the x axis.
        y (int): Position in the universe in the y axis.
    """

    symbol: str = Field(alias="symbol")
    type: WaypointType = Field(alias="type")
    system_symbol: str = Field(alias="systemSymbol")
    x: int = Field(alias="x")
    y: int = Field(alias="y")
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
