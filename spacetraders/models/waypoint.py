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
from pydantic import BaseModel, Field

from ..models.chart import Chart
from ..models.waypoint_faction import WaypointFaction
from ..models.waypoint_orbital import WaypointOrbital
from ..models.waypoint_trait import WaypointTrait
from ..models.waypoint_type import WaypointType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Waypoint")


class Waypoint(BaseModel):
    """A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.

    Attributes:
        symbol (str):
        type (WaypointType): The type of waypoint.
        system_symbol (str):
        x (int):
        y (int):
        orbitals (List['WaypointOrbital']):
        traits (List['WaypointTrait']): The traits of the waypoint.
        faction (Union[Unset, WaypointFaction]):
        chart (Union[Unset, Chart]): The chart of a system or waypoint, which makes the location visible to other
            agents.
    """

    symbol: str = Field(alias="symbol")
    type: WaypointType = Field(alias="type")
    system_symbol: str = Field(alias="systemSymbol")
    x: int = Field(alias="x")
    y: int = Field(alias="y")
    orbitals: List["WaypointOrbital"] = Field(alias="orbitals")
    traits: List["WaypointTrait"] = Field(alias="traits")
    faction: Union[Unset, "WaypointFaction"] = Field(UNSET, alias="faction")
    chart: Union[Unset, "Chart"] = Field(UNSET, alias="chart")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def dict(self, *args, **kwargs):
        output = super().dict(*args, **kwargs)
        return {k: v for k, v in output.items() if v is not UNSET}

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
