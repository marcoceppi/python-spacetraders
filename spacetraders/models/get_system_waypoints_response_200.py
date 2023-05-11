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

from ..models.meta import Meta
from ..models.waypoint import Waypoint
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSystemWaypointsResponse200")


class GetSystemWaypointsResponse200(BaseModel):
    """
    Attributes:
        data (List['Waypoint']):
        meta (Meta):
    """

    data: List["Waypoint"] = Field(alias="data")
    meta: "Meta" = Field(alias="meta")
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
