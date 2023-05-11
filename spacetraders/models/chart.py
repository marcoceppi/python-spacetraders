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
    Union,
    cast,
)

import attr
from dateutil.parser import isoparse
from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Chart")


class Chart(BaseModel):
    """The chart of a system or waypoint, which makes the location visible to other agents.

    Attributes:
        waypoint_symbol (Union[Unset, str]):
        submitted_by (Union[Unset, str]):
        submitted_on (Union[Unset, datetime.datetime]):
    """

    waypoint_symbol: Union[Unset, str] = UNSET
    submitted_by: Union[Unset, str] = UNSET
    submitted_on: Union[Unset, datetime.datetime] = UNSET
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
