from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.waypoint_type import WaypointType
from ..types import Unset

T = TypeVar("T", bound="SystemWaypoint")


class SystemWaypoint(BaseModel):
    """
    Attributes:
        symbol (str):
        type (WaypointType): The type of waypoint.
        x (int):
        y (int):
    """

    symbol: str = Field(alias="symbol")
    type: WaypointType = Field(alias="type")
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
