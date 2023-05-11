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
from pydantic import BaseModel, Field

from ..models.waypoint_type import WaypointType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipNavRouteWaypoint")


class ShipNavRouteWaypoint(BaseModel):
    """The destination or departure of a ships nav route.

    Attributes:
        symbol (str):
        type (WaypointType): The type of waypoint.
        system_symbol (str):
        x (int):
        y (int):
    """

    symbol: str = Field(alias="symbol")
    type: WaypointType = Field(alias="type")
    system_symbol: str = Field(alias="systemSymbol")
    x: int = Field(alias="x")
    y: int = Field(alias="y")
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
