import datetime
from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Chart")


class Chart(BaseModel):
    """The chart of a system or waypoint, which makes the location visible to other agents.

    Attributes:
        waypoint_symbol (Union[Unset, str]): The symbol of the waypoint.
        submitted_by (Union[Unset, str]): The agent that submitted the chart for this waypoint.
        submitted_on (Union[Unset, datetime.datetime]): The time the chart for this waypoint was submitted.
    """

    waypoint_symbol: Union[Unset, str] = Field(UNSET, alias="waypointSymbol")
    submitted_by: Union[Unset, str] = Field(UNSET, alias="submittedBy")
    submitted_on: Union[Unset, datetime.datetime] = Field(UNSET, alias="submittedOn")
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
